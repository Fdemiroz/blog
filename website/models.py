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
	posts = db.relationship('Post', backref='user', passive_deletes=True)

class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	text = db.Column(db.Text, nullable=False)
	created_at = db.Column(db.DateTime(timezone=True), default=func.now())
	author = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)


