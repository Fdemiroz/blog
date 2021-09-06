from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(150), unique=True)
	email = db.Column(db.String(150), unique=True)
	password = db.Column(db.String(150))
	legend = db.Column(db.Boolean, default=False, nullable=False)
	created_at = db.Column(db.DateTime(timezone=True), default=func.now())
