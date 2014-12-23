#File that will call all of the other files and link them together
import Formatter
import Emailer

email = str(raw_input("Enter Email Account: "))
ical = open('OliniCalendar.ics','r')
Emailer.iCalCreator(email, ical)
