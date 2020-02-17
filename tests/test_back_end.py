import unittest

from flask import abort, url_for
from flask_testing import TestCase

from application import app, db
from application.models import Users, Posts

from os import getenv

class TestBase(TestCase):
	def create_app(self):
		config_name = 'testing'				#pass in config for test db
		app.config['SQLALCHEMY_DATABASE_URI'] = str(getenv('TEST_DATABASE'))
		app.config['SECRET_KEY'] = getenv('SKEY')
		return app

	def setUp(self):					#Called before every test
		db.session.commit()				#empties test database at test start
		db.drop_all()
		db.create_all()

								#Creating admin and non-admin tests
		admin = Users(first_name="admin", last_name="admin", email="admin@user.com", password="admin2016")
		employee = Users(first_name="test", last_name="user", email="test@user.com", password="test2016")

		db.session.add(admin)				#Save users to database
		db.session.add(employee)
		db.session.commit()

	def tearDown(self):					#Called after every test
		db.session.remove()
		db.drop_all()

class TestViews(TestBase):					#Test that the homepage is available without login
	def test_homepage_view(self):
		response = self.client.get(url_for('home'))
		self.assertEqual(response.status_code, 200)
