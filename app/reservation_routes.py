from app import db
from app.models.reservation import Reservation
from app.models.reservation_validation import*
from sqlalchemy import Date, cast
from flask import Blueprint, request, jsonify, make_response, abort

from app.models.restaurant import Restaurant

reservation_bp = Blueprint('reservations', __name__,
                           url_prefix="/restaurants/<restaurant_id>")


@reservation_bp.route("/reservations", methods=["POST"])
def create_one_reservation_for_a_restaurant(restaurant_id):
    restaurant = validate_and_return_item(Restaurant, restaurant_id)
    request_body = request.get_json()

    validate_post_request(request_body)

    reservation_slot = validate_date_and_return_datetime(request_body["timestamp"])
    reservation_date = dt.date(reservation_slot.year, reservation_slot.month,
                               reservation_slot.day)

    reservations = Reservation.query.filter(Reservation.restaurant_id == restaurant_id). \
        filter(cast(Reservation.timestamp, Date) == reservation_date).all()

    slots = get_available_slots(reservations, reservation_slot, restaurant.tables)


    is_booking_possible = False
    for slot in slots:
        if slot.hour == reservation_slot.hour:
            is_booking_possible = True

    if is_booking_possible is False:
        return make_response(jsonify(details=f"No available tables for this time. Please choose another time."), 400)

    new_reservation = Reservation(
    customer_name=request_body["customer_name"],
    customer_phone=request_body["customer_phone"],
    timestamp=reservation_slot,
    restaurant_id=restaurant.restaurant_id)

    db.session.add(new_reservation)
    db.session.commit()

    return make_response(jsonify(details=
                f"Reservation with id #{new_reservation.reservation_id} succesfully created"),
                         201)


@reservation_bp.route("/reservations", methods=["GET"])
def get_reservations_for_specific_restaurant(restaurant_id):
    restaurant = validate_and_return_item(Restaurant, restaurant_id)

    reservations = restaurant.reservations

    response = []
    for reservation in reservations:
        response.append({
            "reservation_id": reservation.reservation_id,
            "timestamp": reservation.timestamp,
            "customer_phone": reservation.customer_phone,
            "customer_name": reservation.customer_name,
            "restaurant_id": restaurant.restaurant_id
        })
    return jsonify({
        "restaurant_id": restaurant.restaurant_id,
        "restaurant_name": restaurant.name,
        "reservations": response
    }), 200

@reservation_bp.route("/slots", methods=["GET"])
def get_available_time_slots_for_one_restaurant(restaurant_id):
    restaurant = validate_and_return_item(Restaurant, restaurant_id)
    params = request.args

    reservation_slot = validate_reservation_slot(params)
    reservation_date = dt.date(reservation_slot.year, reservation_slot.month,
                               reservation_slot.day)

    reservations = Reservation.query.filter(
        Reservation.restaurant_id == restaurant_id). \
        filter(cast(Reservation.timestamp, Date) == reservation_date).all()

    slots = get_available_slots(reservations, reservation_slot,
                                restaurant.tables)

    res = []

    for slot in slots:
        res.append(
            slot.__str__()
        )
    return make_response(jsonify({f"{restaurant.name}": {"Available slots": res}}), 200)



@reservation_bp.route("/reservations/<reservation_id>", methods=["DELETE"])
def delete_one_reservation(reservation_id, restaurant_id):
    reservation = validate_and_return_item(Reservation, reservation_id)
    restaurant = validate_and_return_item(Restaurant, restaurant_id)

    db.session.delete(reservation)
    db.session.commit()

    return jsonify(details=f'Deleted reservation with id #{reservation_id} for {restaurant.name}')

