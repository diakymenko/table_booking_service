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

    def to_json(self):
        return {
            "restaurant_id": self.restaurant_id,
            "name": self.name,
            "address": self.address,
            "tables": self.tables,
            "reservations_count": len(self.reservations)
        }
