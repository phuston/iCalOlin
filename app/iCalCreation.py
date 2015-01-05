#This is what will actually create the iCalendar
import random

def iCalWrite(times, yearmonth,endyearmonthdaytime, sdates, dnames, filename):

    ical = open(filename,'w')
    ical.write('BEGIN:VCALENDAR\nPRODID:-//Olin iCalCreation//Python//EN\nVERSION:2.0\n')

# NOW WE GET INTO THE MEATY BUSINESS


    for i in range(len(times)):
        for j in range(len(times[i][0])):
            if times[i][1] != '0000':
                # This essentially just writes a new event for each time slot
                ical.write('BEGIN:VEVENT\n')
                day = sdates[times[i][0][j]]
                ical.write('UUID:'+ yearmonth + day + str( random.randint(100000000,999999999))+'\n')
                ical.write('DTSTART:' + yearmonth + day +'T' + times[i][1] +'00\n')
                ical.write('DTEND:' + yearmonth + day + 'T' + times[i][2] + '00\n')
                ical.write('SUMMARY:' + dnames[i] + '\n')
                ical.write('RRULE:FREQ=WEEKLY;UNTIL='+endyearmonthdaytime + '\n')
                ical.write('END:VEVENT\n')



    # Ending up the ical file with all the business of ending an .ics file.
    ical.write('END:VCALENDAR')


