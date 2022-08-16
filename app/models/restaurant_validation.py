from flask import Blueprint, request, jsonify, make_response, abort

from app.models.restaurant import Restaurant


def validate_post_request_and_return_restaurant(request_body):
    if "name" not in request_body or str(request_body["name"]).split() == []:
        abort(make_response(jsonify(
            {
                "details": "Please enter the name of the restaurant!"
            }), 400))
    if "location" not in request_body or str(request_body["location"]).split() == []:
        abort(make_response(jsonify(
            {
                "details": "Please enter the location of the restaurant!"
            }), 400))
    if "address" not in request_body or str(request_body["address"]).split() == []:
        abort(make_response(jsonify(
            {
                "details": "Please enter the address of the restaurant!"
            }), 400))
    if "tables" not in request_body or str(request_body["tables"]).split() == []:
        abort(make_response(jsonify(
            {
                "details": "Please enter the number of tables!"
            }), 400))

    new_restaurant = Restaurant(
        name=request_body["name"],
        location = request_body["location"],
        address=request_body["address"],
        tables=request_body["tables"]
    )
    if "yelp_id" in request_body:
        new_restaurant.yelp_id=request_body["yelp_id"]

    return new_restaurant


def validate_patch_request_and_return_restaurant(request_body, restaurant):

    if "name" in request_body:
        restaurant.name = request_body["name"]
    if "address" in request_body:
        restaurant.address = request_body["address"]
    if "location" in request_body:
        restaurant.address = request_body["location"]
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