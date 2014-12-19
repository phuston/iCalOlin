from app import app
from flask import render_template, flash, redirect, session, url_for, request, g

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

# @app.route('/', methods=['POST'])
# def index():

#     username = request.form['text']
#     password = request.form['password']
#     email = request.form['emailAddress']
    
#     #Here is where the iCal should go now.


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500