from application import db, login_manager
from flask_login import UserMixin
from datetime import datetime
import random

class Objects(db.Model):
        Line_ID = db.Column(db.Integer, primary_key=True)
	Dayjob = db.Column(db.String(1000), nullable=False, unique=True)
	Expense = db.Column(db.String(1000), nullable=False, unique=True)
	Gift = db.Column(db.String(1000), nullable=False, unique=True)
	Investment = db.Column(db.String(1000), nullable=False, unique=True)
	Charity = db.Column(db.String(100), nullable=False, default="5% of your money has been donated to charity")

# Tables for user functionality

class Posts(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False, unique=True)
	content = db.Column(db.String(1000), nullable=False, unique=True)
	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

	def __repr__(self):
		return ''.join([
			'User ID: ', str(self.user_id), '\r\n',
			'Title: ', self.title, '\r\n', self.content
		])

@login_manager.user_loader
def load_user(id):
	return Users.query.get(int(id))

class Users(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(30), nullable=False)
	last_name = db.Column(db.String(30), nullable=False)
	email = db.Column(db.String(150), nullable=False, unique=True)
	password = db.Column(db.String(200), nullable=False)
	posts = db.relationship('Posts', backref='author', lazy=True)

	def __repr__(self):
		return ''.join([
			'UserID: ', str(self.id), '\r\n',
			'Email: ', self.email, '\r\n',
			'Name: ', self.first_name, ' ', self.last_name
		])

class Content(db.Model):
	c_id = db.Column(db.Integer, primary_key=True)
	rolemodel = db.Column(db.String(50), nullable=False)
	history = db.Column(db.VARCHAR(10000), nullable = False)
	resources = db.Column(db.VARCHAR(5000))
	pictures = db.Column(db.VARCHAR(5000))
