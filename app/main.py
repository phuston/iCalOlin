#File that will call all of the other files and link them together
import getpass
import GetHTML
import Formatter
import iCalCreation
import Emailer
import os

filename = 'OliniCalendar.ics'

# This is the start of the semester:
yearmonth = '201501'
# This is the end of the semester:
endyearmonthdaytime = '20150430T000000'



USERNAME = str(raw_input("Enter my.olin.edu Username: "))
PASSWORD = getpass.getpass('Password:  ')
email = str(raw_input("Email you want it sent to:  "))

htmlResults = GetHTML.htmlHandle(USERNAME,PASSWORD)
num = htmlResults[0]
names = htmlResults[1]
times = htmlResults[2]
locs = htmlResults[3]
timesold = times

times = Formatter.formatTimes(times)


sdates = {'M':'26','T':'20','W':'21','R':'22','F':'23'}

# The following code correlates the classes to each timeslot created from formatTimes. 
# Essentially, I screwed up somewhere and both times for the classes are not kept together and "time slots" are made instead. This just maps each class to it's respective slots.
snames = {}

for i in range(len(timesold)):
    snames[names[i]] = len(timesold[i])

dnames = {}

k = 0
for j in range(7):
    for i in range(snames[names[j]]):
        dnames[k] = names[j]
        k += 1
#Back to normal code

iCalCreation.iCalWrite(times, yearmonth, endyearmonthdaytime, sdates, dnames, filename)
ical = open('OliniCalendar.ics','r')
Emailer.iCalCreator(email,ical)

os.remove('OliniCalendar.ics')
