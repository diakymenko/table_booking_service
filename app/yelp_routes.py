import os

import requests
from flask import Blueprint, jsonify

yelp_bp = Blueprint('yelp', __name__, url_prefix="/yelp")

YELP_URL = "https://api.yelp.com/v3"
YELP_KEY = os.environ.get("YELP_KEY")


@yelp_bp.route('/', defaults={'path': ''})
@yelp_bp.route('/<path:path>')
def proxy(path):
    response = requests.get(
        f'{YELP_URL}/{path}', headers={"Authorization": YELP_KEY}
    )

    return jsonify(response.json()), response.status_code
