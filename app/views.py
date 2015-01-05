from app import app
from flask import render_template, flash, redirect, session, url_for, request, g
from .forms import loginForm
import Emailer, Formatter, GetHTML, iCalCreation

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    username = None
    password = None
    email = None
    form = loginForm()
    if form.validate_on_submit():
        try:
            course_info = GetHTML.htmlHandle(form.username.data,form.password.data)
            # return render_template(html_sched)
            email = form.email.data
            form.username.data = ''
            form.password.data = ''
            form.email.data = ''
            #Here is where iCal creation and emailing should happen
        except:
            print("oops")
    return render_template('index.html', form=form)


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500