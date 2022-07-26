from flask import Blueprint, request, jsonify, make_response, abort

from app import db
from app.models.restaurant import Restaurant

restaurant_bp = Blueprint('restaurants', __name__, url_prefix="/restaurants")


@restaurant_bp.route("", methods=["POST"])
def create_restaurant():
    request_body = request.get_json()

    if "name" not in request_body:
        return jsonify(
            {
                "details": "Please enter the name of the restaurant!"
            }), 400
    if "address" not in request_body:
        return jsonify(
            {
                "details": "Please enter the address of the restaurant!"
            }), 400
    if "tables" not in request_body:
        return jsonify(
            {
                "details": "Please enter the number of tables!"
            }), 400

    new_restaurant = Restaurant(
        name=request_body["name"],
        address=request_body["address"],
        tables=request_body["tables"]
    )

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


@restaurant_bp.route("/<restaurant_id>", methods=["GET"])
def get_restaurant_by_id(restaurant_id):
    restaurant = validate_and_return_item(Restaurant, restaurant_id)
    return make_response(restaurant.to_json(), 200)


@restaurant_bp.route("/<restaurant_id>", methods=["PATCH"])
def update_restaurant(restaurant_id):
    restaurant = validate_and_return_item(Restaurant, restaurant_id)
    request_body = request.get_json()

    if "name" in request_body:
        restaurant.name = request_body["name"]
    if "address" in request_body:
        restaurant.address = request_body["address"]
    if "tables" in request_body:
        restaurant.tables = request_body["tables"]

    db.session.add(restaurant)
    db.session.commit()

    return make_response(restaurant.to_json(), 200)


@restaurant_bp.route("/<restaurant_id>", methods=["DELETE"])
def delete_restaurant(restaurant_id):
    restaurant = validate_and_return_item(Restaurant, restaurant_id)

    db.session.delete(restaurant)
    db.session.commit()

    return make_response(jsonify(details=
                                 f'Restaurant {restaurant.nmae} with id #{restaurant.restaurant_id} successfully deleted'),
                         204)


def validate_and_return_item(cls, item_id):
    try:
        item_id = int(item_id)
    except ValueError:
        abort(make_response(jsonify({
            "details": f'Invalid data for {cls.cls_name()} with id #{item_id}'})),
            400)
    item = cls.query.get(item_id)
    if item:
        return item
    abort(make_response(
        {"details": f'{cls.cls_name()} with id #{item_id} not found'}, 404))
