from flask import Blueprint, request, jsonify, make_response, abort
from app.models.reservation_utils import*
from app.models.reservation_validation import*
from sqlalchemy import Date, cast

def validate_post_request(request_body):

    if "customer_name" not in request_body or str(request_body["customer_name"]).split() == []:
        abort(make_response(jsonify(
            {
                "details": "Please enter a customer name for the reservation!"
            }), 400))
    if "customer_phone" not in request_body or str(request_body["customer_phone"]).split() == []:
        abort(make_response(jsonify(
            {
                "details": "Please enter a customer phone number for the reservation!"
            }), 400))
    if "timestamp" not in request_body or str(request_body["timestamp"]).split() == []:
        abort(make_response(jsonify(
            {
                "details": "Please enter date and time for the reservation!"
            }), 400))

def validate_date_and_return_datetime(date):
    try:
        date_obj = dt.datetime.strptime(date,'%Y-%m-%d-%H')
    except ValueError:
        abort(make_response(
            jsonify({
                "details": f'Invalid format for date. Please use "%Y-%m-%d-%H" format'}),
            400))
    if date_obj:
        if date_obj < dt.datetime.now():
            abort(make_response(
                    {"details": f'The date and time cannot be in the past!'}, 400))
        else:
            return date_obj


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
        make_response({"details": f'{cls.cls_name()} with id #{item_id} not found'}, 404))

def validate_reservation_slot(params):
    if "date" not in params:
        reservation_slot = dt.datetime.now()
    else:
        reservation_slot = validate_date_and_return_datetime(
        params["date"])
    return reservation_slot