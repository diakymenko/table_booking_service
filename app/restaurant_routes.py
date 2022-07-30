from app.models.restaurant_validation import*

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


@restaurant_bp.route("/<restaurant_id>", methods=["GET"])
def get_restaurant_by_id(restaurant_id):
    restaurant = validate_and_return_item(Restaurant, restaurant_id)
    return make_response(restaurant.to_json(), 200)


@restaurant_bp.route("/<restaurant_id>", methods=["PATCH"])
def update_restaurant(restaurant_id):
    restaurant = validate_and_return_item(Restaurant, restaurant_id)
    request_body = request.get_json()
    restaurant = validate_patch_request_and_return_restaurant(request_body, restaurant)

    db.session.add(restaurant)
    db.session.commit()

    return make_response(restaurant.to_json(), 200)


@restaurant_bp.route("/<restaurant_id>", methods=["DELETE"])
def delete_restaurant(restaurant_id):
    restaurant = validate_and_return_item(Restaurant, restaurant_id)

    db.session.delete(restaurant)
    db.session.commit()

    return jsonify({'msg': f'Deleted restaurant with id {restaurant_id}'}),200

