#This is what will actually create the iCalendar
import Formatter
import Emailer
import random

ical = open('OliniCalendar.ics','w')

# Importing all the names of different things because this is what made sense at the time
num = Formatter.num
names = Formatter.names
times = Formatter.times

# Jank code that needs to be fixed at one point
timesold = Formatter.timesold
locs = Formatter.locs

# Maps the day in the week to the actual starting date of 2015 spring semester
# NOTE: this is only a temporary fix, needs to be redone for each semester
sdates = {'M':'26','T':'20','W':'21','R':'22','F':'23'}


# THE FOLLOWING CODE IS JANKY
'''
What it does is fix an issue with how the dates are recorded, which happens to seperate the times from separate days for the same class. What this code does it maps the classes to a number of time slots, which will then correlate to which days are mapped to it. When the actual writing is done, the time slot is called for the time which maps to a certain class.

If that made no sense,
 Timeslot 1 = Modsim
 Timeslot 2 = Modsim
 Timeslot 3 = new class


When it should be 
 [Times1, Times2] = Modsim
 [Times1] = new class

This code is fixable in the Formatting.py, however it will be functional for all times using this code. 

'''
snames = {}

for i in range(len(timesold)):
    snames[names[i]] = len(timesold[i])

dnames = {}

k = 0
for j in range(7):
    for i in range(snames[names[j]]):
        dnames[k] = names[j]
        k += 1
# END OF JANK CODE


# Look at me commenting code. I wonder what this string is....
yearmonth = '201501'

# Initializing the .ics file with the header stuff
ical.write('BEGIN:VCALENDAR\nPRODID:-//Olin iCalCreation//Python//EN\nVERSION:2.0\n')

# NOW WE GET INTO THE MEATY BUSINESS


for i in range(len(times)):
    for j in range(len(times[i][0])):
        if times[i][1] != '0000':
            ical.write('BEGIN:VEVENT\n')
            day = sdates[times[i][0][j]]
            ical.write('UUID:'+ yearmonth + day + str( random.randint(100000000,999999999))+'\n')
            ical.write('DTSTART:' + yearmonth + day +'T' + times[i][1] +'00\n')
            ical.write('DTEND:' + yearmonth + day + 'T' + times[i][2] + '00\n')
            ical.write('SUMMARY:' + dnames[i] + '\n')
            ical.write('RRULE:FREQ=WEEKLY\n')
            ical.write('END:VEVENT\n')



# Ending up the ical file with all the business of ending an .ics file.
ical.write('END:VCALENDAR')

email = str(raw_input("Enter Email Account: "))
ical = open('OliniCalendar.ics','r')
Emailer.iCalCreator(email,ical)

''' THIS IS WHAT NEEDS TO BE DONE

BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Olin iCalCreation//python/EN
BEGIN:VEVENT
UID: { SOME RANDOM STRING }
DTSTART:{year}{month}{day}T{Time in 24hour format + a 0 at the end (?)}
DTEND:^
SUMMARY:{Name of event}
RRULE:FREQ=WEEKLY
END:VEVENT
END:VCALENDAR

'''

