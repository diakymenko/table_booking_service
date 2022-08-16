from app.models.reservation import Reservation
from app.models.reservation_validation import *
from app.models.restaurant import *
from app.models.restaurant_validation import *

restaurant_bp = Blueprint('restaurants', __name__, url_prefix="/restaurants")


@restaurant_bp.route("", methods=["POST"])
def create_restaurant():
    request_body = request.get_json()
    new_restaurant = validate_post_request_and_return_restaurant(request_body)

    db.session.add(new_restaurant)
    db.session.commit()

    return make_response(jsonify(details=
                                 f"Restaurant {new_restaurant.name} with id {new_restaurant.restaurant_id} successfully created"),
                         201)


@restaurant_bp.route("", methods=["GET"])
def read_all_restaurants():
    restaurants = Restaurant.query.all()

    restaurants_response = []
    for restaurant in restaurants:
        restaurants_response.append(restaurant.to_json())
    return make_response(jsonify(restaurants_response), 200)


@restaurant_bp.route("/<location>", methods=["GET"])
def read_restaurants_slots_for_location_and_datetime(location):
    params = request.args
    restaurants = db.session.query(Restaurant).filter_by(
        location=location).all()

    reservation_slot = validate_reservation_slot(params)
    reservation_date = dt.date(reservation_slot.year, reservation_slot.month,
                               reservation_slot.day)
    res = []
    for restaurant in restaurants:
        reservations_list = []

        reservations = Reservation.query.filter(
            Reservation.restaurant_id == restaurant.restaurant_id).filter(
            cast(Reservation.timestamp, Date) == reservation_date).all()
        slots = get_available_slots(reservations, reservation_slot,
                                    restaurant.tables)

        for slot in slots:
            reservations_list.append(
                slot.__str__()
            )
        res.append({"id": restaurant.restaurant_id,
                    "name": restaurant.name,
                    "location": restaurant.location,
                    "address": restaurant.address,
                    "available_slots": reservations_list,
                    "yelp_id": restaurant.yelp_id,
                    "reservations_count": len(restaurant.reservations)
                    })
    return jsonify(res)


@restaurant_bp.route("/<restaurant_id>", methods=["GET"])
def get_restaurant_by_id(restaurant_id):
    restaurant = validate_and_return_item(Restaurant, restaurant_id)
    return make_response(restaurant.to_json(), 200)


@restaurant_bp.route("/<restaurant_id>", methods=["PATCH"])
def update_restaurant(restaurant_id):
    restaurant = validate_and_return_item(Restaurant, restaurant_id)
    request_body = request.get_json()
    restaurant = validate_patch_request_and_return_restaurant(request_body,
                                                              restaurant)

    db.session.add(restaurant)
    db.session.commit()

    return make_response(restaurant.to_json(), 200)


@restaurant_bp.route("/<restaurant_id>", methods=["DELETE"])
def delete_restaurant(restaurant_id):
    restaurant = validate_and_return_item(Restaurant, restaurant_id)

    db.session.delete(restaurant)
    db.session.commit()

    return jsonify({'msg': f'Deleted restaurant with id {restaurant_id}'}), 200
