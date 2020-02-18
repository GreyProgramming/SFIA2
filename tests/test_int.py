import unittest
import time
from flask import url_for
from urllib.request import urlopen

from os import getenv
from flask_testing import LiveServerTestCase as LSTC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from application import app, db, bcrypt
from application.models import Users

test_admin_first_name = "admin"												# Setting test variables
test_admin_last_name = "Admin"
test_admin_email = "Admin@admin.admin"
teat_admin_password = "1Admin2Admin3Admin4!"

class TestBase(LSTC):
	def create_app(self):												#Defining methods
		app.config['SQLALCHEMY_DATABASE_URI'] = str(getenv('TEST_DATABASE'))
		app.config['SECRET_KEY'] = getenv('SKEY')
		return app

	def setUp(self):												#Set up test driver + create next user
		print("----------Next-Test----------")
		chrome_options = Options()
		chrome_options.binary_location = "/usr/bin/google-chrome-stable"
		chrome_options.add_argument("--headless")
		chrome_options.add_argument("--no-sandbox")
		chrome_options.add_argument("disable-gpu")
		chrome_options.add_argument("window-size=1920,1080")
		chrome_options.add_argument("disable-dev-shm-usage")
		chrome_options.add_argument("disable-features=VizDisplayCompositor")
		self.driver = webdriver.Chrome(executable_path="/home/morgangreyprofessional/flask-app/chromedriver", chrome_options=chrome_options)
		self.driver.get("http://localhost:5000")
		db.session.commit()
		db.drop_all()
		db.create_all()

	def tearDown(self):
		self.driver.quit()
		print("----------End-Of-Test----------\n\n\n----------Unit-And-Selenium-Tests----------")


	def TestServerRunning(self):
		response = urlopen("http://localhost:5000")
		self.assertEqual(response.status_code, 200)

class TestRegistration(TestBase):
	def test_registration(self):
		self.driver.find_element_by_xpath("/html/body/div[1]/a[3]").click()			#nav to Register
		time.sleep(5)

		self.driver.find_element_by_xpath('/html/body/div[2]/form/div[3]/div[2]/input').send_keys(test_admin_email)		#fill in form
		self.driver.find_element_by_xpath('/html/body/div[2]/form/div[1]/div[2]/input').send_keys(test_admin_first_name)
		self.driver.find_element_by_xpath('/html/body/div[2]/form/div[2]/div[2]/input').send_keys(test_admin_last_name)
		self.driver.find_element_by_xpath('/html/body/div[2]/form/div[4]/div[2]/input').send_keys(test_admin_password)
		self.driver.find_element_by_xpath('/html/body/div[2]/form/div[5]/div[2]/input').send_keys(test_admin_password)
		self.driver.find_element_by_xpath('/html/body/div[2]/form/div[6]/input').click()
		time.sleep(1)

		assert url_for('login') in self.driver.current_url							#check that browser redirects to login

if __name__ == '__main__':
	unittest.main(port=5000)
