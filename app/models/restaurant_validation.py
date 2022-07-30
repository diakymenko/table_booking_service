from flask import Blueprint, request, jsonify, make_response, abort

from app.models.restaurant import Restaurant
from app.models.restaurant_validation import*


def validate_post_request_and_return_restaurant(request_body):
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
    return new_restaurant


def validate_patch_request_and_return_restaurant(request_body, restaurant):

    if "name" in request_body:
        restaurant.name = request_body["name"]
    if "address" in request_body:
        restaurant.address = request_body["address"]
    if "tables" in request_body:
        restaurant.tables = request_body["tables"]

    return restaurant

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