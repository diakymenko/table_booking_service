import datetime

from app import db


class Reservation(db.Model):
    reservation_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    timestamp = db.Column(db.DateTime(timezone=True),
                          default=datetime.datetime.utcnow)
    customer_name = db.Column(db.String)
    customer_phone = db.Column(db.String)
    restaurant_id = db.Column(db.Integer,
                              db.ForeignKey('restaurant.restaurant_id'))

    @classmethod
    def cls_name(cls):
        return "reservation"

    def to_json(reservation):
        return {
            "reservation_id":reservation.reservation_id,
            "timestamp": reservation.timestamp,
            "customer_name": reservation.customer_name,
            "customer_phone": reservation.customer_phone,
            "restaurant_id": reservation.restaurant_id,
        }
