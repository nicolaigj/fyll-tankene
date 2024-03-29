from flask import render_template, redirect, flash
from app import app
from flask_login import login_user, logout_user, login_required, current_user
from .forms import LoginForm 
from .models import User

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect('/index')
        flash('Username or password is incorrect')
    return render_template('login.html', form=form)