from app import app
from flask import render_template, flash, redirect, session, url_for, request, g
from .forms import loginForm

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    username = None
    password = None
    email = None
    form = loginForm()
    if form.validate_on_submit():
    	username = form.username.data
        password = form.password.data
        email = form.email.data
        form.username.data = ''
        form.password.data = ''
        form.email.data = ''
    return render_template('index.html', form=form)


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500