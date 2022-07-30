import datetime

from app import db


class Reservation(db.Model):
    reservation_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    timestamp = db.Column(db.DateTime(timezone=False),
                          default=datetime.datetime.now())
    customer_name = db.Column(db.String)
    customer_phone = db.Column(db.String)
    restaurant_id = db.Column(db.Integer,
                              db.ForeignKey('restaurant.restaurant_id'))

    @classmethod
    def cls_name(cls):
        return "reservation"

    def to_json(self):
        return {
            "reservation_id":self.reservation_id,
            "timestamp": self.timestamp,
            "customer_name": self.customer_name,
            "customer_phone": self.customer_phone,
            "restaurant_id": self.restaurant_id,
        }
