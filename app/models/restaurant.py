from app import db


class Restaurant(db.Model):
    restaurant_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    address = db.Column(db.String)
    tables = db.Column(db.Integer)
    reservations = db.relationship("Reservation", backref="restaurant",
                                   lazy=True)

    @classmethod
    def cls_name(cls):
        return "restaurant"

    def to_json(restaurant):
        return {
            "restaurant_id": restaurant.restaurant_id,
            "name": restaurant.name,
            "address": restaurant.address,
            "tables": restaurant.tables,
            "reservations_count": len(restaurant.reservations)
        }
