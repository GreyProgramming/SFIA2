from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from application.models import Users

class PostForm(FlaskForm):
	title = StringField('Title',
		validators = [
			DataRequired(),
			Length(min=2, max=100)
		]
	)
	content = StringField('Content',
		validators = [
			DataRequired(),
			Length(min=100, max=1000)
		]
	)
	submit = SubmitField('Send submission!')

class RegistrationForm(FlaskForm):
	first_name = StringField('First Name',
		validators = [
			DataRequired(),
			Length(min=2, max=30)
		]
	)
	last_name = StringField('Last Name',
		validators = [
			DataRequired(),
			Length(min=2, max=30)
		]
	)
	email = StringField('Email',
		validators = [
			DataRequired(),
		]
	)
	password = PasswordField('Password',
		validators = [
			DataRequired(),
		]
	)
	confirm_password = PasswordField('Confirm your Password',
		validators = [
			DataRequired(),
			EqualTo('password')
		]
	)
	submit = SubmitField('Sign Up')

	def validate_email(self, email):
		user = Users.query.filter_by(email=email.data).first()

		if user:
			raise ValidatorError('That email is already in use, my dude.')

class LoginForm(FlaskForm):
	email = StringField('Email',
		validators=[
			DataRequired(),
			Email()
		]
	)

	password = PasswordField('Password',
		validators=[
			DataRequired()
		]
	)

	remember = BooleanField('Remember your login?')
	submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
	first_name = StringField('First Name',
		validators=[
			DataRequired(),
			Length(min=2, max=30)
		])
	last_name = StringField('Last Name',
		validators=[
			DataRequired(),
			Length(min=2, max=30)
		])
	email = StringField('Email',
		validators=[
			DataRequired(),
			Email()
		])
	submit = SubmitField('Update')

	def validate_email(self,email):
		if email.data != current_user.email:
			user = Users.query.filter_by(email=email.data).first()
			if user:
				raise ValidationError('Email already in use')