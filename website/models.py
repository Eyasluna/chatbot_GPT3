from . import db


class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.String(20))
    message = db.Column(db.String(500))
    message_type = db.Column(db.String(100))
