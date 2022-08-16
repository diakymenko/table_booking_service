import requests
from flask import Blueprint

ip_bp = Blueprint('ip', __name__, url_prefix="/ip")
IP_URL = "https://api64.ipify.org?format=json"
LOCATION_URL = "https://ipapi.co"


@ip_bp.route("", methods=["GET"])
def get_user_location():
    response = requests.get(IP_URL)
    ip = response.json()["ip"]

    loc_response = requests.get(f'{LOCATION_URL}/{ip}/json')

    return {"city": loc_response.json()["city"]}, loc_response.status_code
