from website import db


class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime, nullable=False)
    message = db.Column(db.String(200), nullable=False)
    message_type = db.Column(db.String(50), nullable=False)
