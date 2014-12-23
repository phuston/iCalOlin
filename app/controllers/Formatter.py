import sys
import random
import pytz
# Setting up the program for writing the calendar files

# Uncomment this section and comment the next section in order to switch to real mode

import GetHTML
num = GetHTML.num
names = GetHTML.names
times = GetHTML.times
locs = GetHTML.locs


# Setting up variables for testing purposes, uncomment import GetHTML in order to read real values
'''
num = 7

names = ['The Wired Ensemble -Instruments, Voices, Players', 'Do Machine Learning', 'Introduction to Sensors, Instrumentation and Measurement', 'Design Nature', 'Modeling and Simulation of the Physical World', 'Olin Introductory Experience', 'Modeling and Simulation of the Physical World']

times = [['F -10:50AM - 12:30 PM', 'T -3:20 - 5:00 PM'], ['-0:00 - 0:00 AM'], ['R -1:00 - 3:10 PM', 'M -1:30 - 3:10 PM'], ['MW -3:20 - 6:00 PM'], ['MR -10:50AM - 12:30 PM'], ['R -3:20 - 5:00 PM'], ['W -9:00 - 10:40 AM', 'W -9:00 - 10:40 AM']]

locs = ['Location feature not yet implemented', 'Location feature not yet implemented', 'Location feature not yet implemented', 'Location feature not yet implemented', 'Location feature not yet implemented', 'Location feature not yet implemented', 'Location feature not yet implemented']

'''

#Starting some jank-ass code in order to have classes on multiple days. 
timesold = times

# Starting the actual code
def formatTimes(t):
    time = []
    for i in range(len(t)):
        for j in range( len(t[i])):
            tmp = t[i][j]
            tmp = tmp.replace('-','', 1)
            tmp = tmp.replace(' ','')
            tmp = tmp.replace(':','')
            
            tmp = tmp.split('-')            
            day = []
            
            # Fixing up the 1st time values to be in 24 hr format and stripping data
            if 'AM' in tmp[0] or 'AM' in tmp[1]:
                tmp[0] = tmp[0].replace('AM','')
                tmp[0] = tmp[0].replace(':','')
                for l in tmp[0]:
                    if l in 'MTWRF':
                        date = tmp[0][tmp[0].find(l)]
                        day.append(tmp[0][tmp[0].find(l)])
                        tmp[0] = tmp[0].replace(date,'')
                if len(tmp[0]) < 4:
                    tmp[0] = '0' + tmp[0]

            else:
                tmp[0] = tmp[0].replace('PM','')
                tmp[0] = tmp[0].replace(':','')
                for l in tmp[0]:
                    if l in 'MTWRF':
                        date = tmp[0][tmp[0].find(l)]
                        day.append(tmp[0][tmp[0].find(l)])
                        tmp[0] = tmp[0].replace(date,'')
                tmp[0] = int(tmp[0])
                if tmp[0] < 1100: tmp[0] = tmp[0] + 1200
                tmp[0] = str(tmp[0])



            # Fixing up the 2nd time values to be in 24 hr format and stripping of all other stuff
            if 'AM' in tmp[1]:
                tmp[1] = tmp[1].replace('AM','')
                if len(tmp[1]) < 4: tmp[1] = '0' + tmp[1]
                
            else:
                tmp[1] = tmp[1].replace('PM','')
                tmp[1] = int(tmp[1])
                if tmp[1] < 1100:
                    tmp[1] = tmp[1] + 1200
                tmp[1] = str(tmp[1])
            

            #print tmp
            #print day
            timetmp = [day]+tmp
            time.append(timetmp)
    return time

times = formatTimes(times)


# No longer single commented out lines, I believe this is the implementation of the iCal code
'''
def SetEvent(course, time, location):
    
    timef = time.split(';',5)
    locationf = location.split(';',5)

    startevent = "BEGIN:VEVENT\n"
    
    cal = Calendar()
    from datetime import datetime
    cal.add('prodid','-//My calendar product//mxm.dk//')
    cal.add('version','2.0')
    
    event = Event()
    event.add('summary',course)
    event.add('dstart',datetime(2014,
    return event
'''

# Haven't fleshed out what this stuff does yet
'''
dataout = open('testcalendar.ical','w') # The file to write data


#Begining the writout of events
starter = ('BEGIN:VCALENDAR\n'
'VERSION:2.0\n'
'PRODID:-//bobbin v0.1//NONSGML iCal Writer//EN\n'
'CALSCALE:GREGORIAN\n'
'METHOD:PUBLISH\n')

for i in range(0,numbcourse ):
    SetEvent(data[1+3*i],data[2+3*i],data[3+3*i])

dataout.write(starter)

'''
