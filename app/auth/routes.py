from flask import render_template, flash, redirect, url_for
from app.auth.forms import RegistrationForm, LoginForm
from app.auth import authentication as at
from app.auth.models import User
from flask_login import login_user, logout_user, login_required, current_user


# This route can be a get or a post method, by default it is get

@at.route('/register', methods=['GET', 'POST'])
def register_user():

    # check if user is already logged in flask_login method

    if current_user.is_authenticated:
        flash('You are already logged-in')
        return redirect(url_for('main.display_books'))

    form = RegistrationForm()

    '''
    name = None
    email = None
    # used in the registration page
    if request.method == 'POST':
        name = form.name.data
        email = form.email.data
    '''

    # it is better to use the below method since the forms will be validated and checked if its a POST

    if form.validate_on_submit():
        User.create_user(
            user=form.name.data,
            email=form.email.data,
            password=form.password.data)
        # post a message to user
        flash('Registration Successful')

        # redirect to user login page by using url_for, create a link instead of hardc oding
        return redirect(url_for('authentication.login_user'))
    return render_template('registration.html', form=form)

@at.route('/login', methods=['GET', 'POST'])
def do_the_login():

    if current_user.is_authenticated:
        flash('You are already logged-in')
        return redirect(url_for('main.display_books'))

    # create a form to enter in the data.
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(user_email=form.email.data).first()

        # redirect on failed attempt
        if not user or not user.check_password(form.password.data):
            flash('Invalid Credentials, Please try again')
            return redirect(url_for('authentication.do_the_login'))

        login_user(user, form.stay_loggedin.data)
        return redirect(url_for('main.display_books'))
    return render_template('login.html', form=form)


# multiple decorators when used, the execution is from top to bottom, logout and then login_required.
@at.route('/logout')

# this decorator is used, to make sure user is already logged in.
@login_required
def log_out_user():
    logout_user()
    return redirect(url_for('main.display_books'))

# this can be at any routes file in any package in the app.
@at.app_errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404