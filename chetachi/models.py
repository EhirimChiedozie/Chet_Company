from chetachi import db
from datetime import datetime

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    current_location = db.Column(db.String(500), nullable=False)
    phonenumber1 = db.Column(db.String(20), nullable=False)
    phonenumber2 = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    date_ordered = db.Column(db.DateTime, default=datetime.utcnow)
    def __repr__(self):
        return f"customer('{self.name}', '{self.current_location}', '{self.phonenumber1}', '{self.phonenumber2}', '{self.description}', '{self.date_ordered}')"
