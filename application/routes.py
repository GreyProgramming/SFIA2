from flask import render_template, redirect, url_for, request
from flask_login import login_user, current_user, logout_user, login_required

from application import app, db, bcrypt
from application.models import Posts, Users, Content
from application.forms import PostForm, RegistrationForm, LoginForm, UpdateAccountForm


@app.route('/')
@app.route('/home')
def home():
	postData = Posts.query.all()
	return render_template('home.html', title='Home', posts=reversed(postData))

@app.route('/about')
def about():
	return render_template('about.html', title='About')

@app.route('/register', methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = RegistrationForm()
	if form.validate_on_submit():
		hash_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = Users(
			first_name = form.first_name.data,
			last_name = form.last_name.data,
			email = form.email.data,
			password = hash_pw
		)

		db.session.add(user)
		db.session.commit()

		return redirect(url_for('post'))
	return render_template('register.html', title='Registration', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:							#Checks to see if the user is already logged in
		return redirect(url_for('home'))
	form = LoginForm()
	if form.validate_on_submit():
		user=Users.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):	#Checks if user and password are linked
			login_user(user, remember=form.remember.data)				#If correct, logs user in, remembers if ticked
			next_page = request.args.get('next')
			if next_page:
				return redirect(next_page)
			else:
				return redirect(url_for('home'))
	return render_template('login.html', title='Login', form=form)

@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
	form = UpdateAccountForm()
	posts = Posts.query.filter_by(user_id=current_user.id).all()
	if form.validate_on_submit():
		current_user.first_name = form.first_name.data
		current_user.last_name = form.last_name.data
		current_user.email = form.email.data
		db.session.commit()
		return redirect(url_for('account'))
	elif request.method == 'GET':
		form.first_name.data = current_user.first_name
		form.last_name.data = current_user.last_name
		form.email.data = current_user.email
	return render_template('account.html', title='Account', form=form, posts=posts)

@app.route('/account/delete', methods=['GET', 'POST'])
@login_required
def account_delete():
	user = current_user.id
	account = Users.query.filter_by(id=user).first()
	posts = Posts.query.filter_by(user_id=user).all()
	for post in posts:
		db.session.delete(post)
	logout_user()
	db.session.delete(account)
	db.session.commit()
	return redirect(url_for('register'))

@app.route("/viewer/<id>")
def view(id):
        RM = Content.query.filter_by(c_id=id).first()
        if RM:
                print(RM.rolemodel)
                return render_template('viewer.html', RM=RM)
        else:
                return redirect(url_for('post'))

@app.route("/update/<id>", methods=['GET', 'POST'])
def postupd(id):
	UDP = Posts.query.filter_by(id=id).first()
	form = PostForm()
	if UDP.user_id == current_user.id:
		if form.validate_on_submit():
			UDP.title = form.title.data
			UDP.content = form.content.data
			db.session.add(UDP)
			db.session.commit()
			return redirect(url_for('account'))
		form.title.data = UDP.title
		form.content.data = UDP.content
		return render_template('updates.html', title="Update Post", form=form, post=UDP)
	return "That's not your post"

@app.route("/update/delete/<id>", methods=['GET', 'POST'])
@login_required
def postdel(id):
	post = Posts.query.filter_by(id=id).first()
	db.session.delete(post)
	db.session.commit()
	return redirect(url_for('account'))

@app.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('login'))

@app.route('/post', methods=['GET', 'POST'])
@login_required
def post():
	form = PostForm()
	if form.validate_on_submit():
		postData = Posts(
			title = form.title.data,
			content = form.content.data,
			author = current_user
		)
		db.session.add(postData)
		db.session.commit()
		return redirect(url_for('home'))
	else:
			print(form.errors)
	return render_template('post.html', title = 'Post', form=form)

@app.route("/<name>", methods=['GET', 'POST'])
def user(name):
	search = "%{}%".format(name)
	RM = Content.query.filter(Content.rolemodel.like(search)).first()
	if not RM:
		if current_user.is_authenticated:
			form = PostForm()
			form.title.data = name
			if form.validate_on_submit():
				postData = Posts(
					title = form.title.data,
					content = form.content.data,
					author = current_user
				)
				db.session.add(postData)
				db.session.commit()
				return redirect(url_for('home'))
			else:
				print(form.errors)
		else:
			return redirect(url_for('login'))

	else:
		return redirect(url_for('view', id=RM.c_id))
