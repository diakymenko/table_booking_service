import os

from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config['CORS_HEADERS'] = 'Content-Type'

    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
        "SQLALCHEMY_DATABASE_URI")

    # from app.models.restaurant import Restaurant
    # from app.models.reservation import Reservation

    db.init_app(app)
    migrate.init_app(app, db)

    from .restaurant_routes import restaurant_bp
    app.register_blueprint(restaurant_bp)

    from .reservation_routes import reservation_bp
    app.register_blueprint(reservation_bp)

    return app
