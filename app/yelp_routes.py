from flask import Blueprint, jsonify

import requests

yelp_bp = Blueprint('yelp', __name__, url_prefix="/yelp")

YELP_URL = "https://api.yelp.com/v3"
YELP_KEY = "Bearer JRDYbAT6wkFWpEEtt0HGXf1bibl8lixu6MYbQbMal_n6oC2i9_AKo4lQzx_RXIeN2W0uISGpAsHLwT0jgk2zJs9JZ-1NojqYGo5-XI1E4jjaQMPPx0wfur6KGaryYnYx"


@yelp_bp.route('/', defaults={'path': ''})
@yelp_bp.route('/<path:path>')
def proxy(path):
    response = requests.get(
        f'{YELP_URL}/{path}', headers={"Authorization": YELP_KEY}
    )

    return jsonify(response.json()), response.status_code
