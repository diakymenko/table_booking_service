from flask import Blueprint, request, jsonify, make_response, abort

from app import db
from app.models.reservation import Reservation
from app.models.restaurant import Restaurant

reservation_bp = Blueprint('reservations', __name__,
                           url_prefix="/restaurants/<restaurant_id>/reservations")


@reservation_bp.route("", methods=["POST"])
def create_one_reservation_for_a_restaurant(restaurant_id):
    request_body = request.get_json()
    restaurant = validate_and_return_item(Restaurant, restaurant_id)

    if "customer_name" not in request_body:
        return jsonify(
            {
                "details": "Please enter a customer name for the reservation!"
            }), 400
    if "customer_phone" not in request_body:
        return jsonify(
            {
                "details": "Please enter a customer phone number for the reservation!"
            }), 400

    new_reservation = Reservation(
        customer_name=request_body["customer_name"],
        customer_phone=request_body["customer_phone"],
        restaurant_id=restaurant.restaurant_id)

    if "timestamp" in request_body:
        new_reservation.timestamp = request_body["timestamp"]

    db.session.add(new_reservation)
    db.session.commit()

    return make_response(jsonify(details=
        f"Reservation with id #{new_reservation.reservation_id} succesfully created"),
                         201)


@reservation_bp.route("", methods=["GET"])
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


def validate_and_return_item(cls, item_id):
    try:
        item_id = int(item_id)
    except ValueError:
        abort(make_response(
            jsonify({"details": f'Invalid data for {cls.cls_name()} with id #{item_id}'})),
              400)
    item = cls.query.get(item_id)
    if item:
        return item
    abort(
        make_response({"details": f'{cls} with id #{item_id} not found'}, 404))


@reservation_bp.route("/<reservation_id>", methods=["PATCH"])
def update_reservation_for_specific_restaurant(restaurant_id, reservation_id):
    restaurant = validate_and_return_item(Restaurant, restaurant_id)
    reservation = validate_and_return_item(Reservation, reservation_id)

    request_body = request.get_json()

    if "timestamp" in request_body:
        reservation.timestamp = request_body["timestamp"]
    if "customer_name" in request_body:
        reservation.customer_name = request_body["customer_name"]
    if "customer_phone" in request_body:
        reservation.customer_phone = request_body["customer_phone"]

    db.session.commit()

    return make_response(jsonify(details=
        f"Reservation with id #{reservation.reservation_id} for {restaurant.name} succesfully updated"),
        201)


@reservation_bp.route("/<reservation_id>", methods=["DELETE"])
def delete_one_card(reservation_id, restaurant_id):
    reservation = validate_and_return_item(Reservation, reservation_id)
    restaurant = validate_and_return_item(Restaurant, restaurant_id)

    db.session.delete(reservation)
    db.session.commit()

    return jsonify(details=f'Deleted reservation with id #{reservation_id} for {restaurant.name}')
