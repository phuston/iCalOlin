from app import app
from flask import render_template, flash, redirect, session, url_for, request, g
from .forms import loginForm
import Emailer, Formatter, GetHTML, iCalCreation
import os

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

            timesold = course_info[2]
            names = course_info[1]
            course_info[2] = Formatter.formatTimes(course_info[2])
            sdates = {'M':'26','T':'20','W':'21','R':'22','F':'23'}

            snames = {}

            for i in range(len(timesold)):
                snames[names[i]] = len(timesold[i])

            dnames = {}

            k = 0
            for j in range(7):
                for i in range(snames[names[j]]):
                    dnames[k] = names[j]
                    k += 1

            filename = 'OliniCalendar.ics'

            iCalCreation.iCalWrite(course_info[2],"201501","20150430T000000",sdates,dnames,filename)

            ical = open('OliniCalendar.ics','r')

            email = form.email.data
            Emailer.iCalCreator(email,ical)

            os.remove('OliniCalendar.ics')
            # return render_template(html_sched)
            
            form.username.data = ''
            form.password.data = ''
            form.email.data = ''
        except:
            "Oops"

    return render_template('index.html', form=form)


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404
