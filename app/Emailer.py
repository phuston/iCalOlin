import smtplib, os

from email.MIMEMultipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate
from email import Encoders


def iCalCreator (email, ical):

	# Addresses and subjects
	fromaddr = 'iCalCreator@gmail.com'
	toaddrs  = email
	subject = 'Your iCal Schedule!'

	#Mulit-Part message
	msg = MIMEMultipart()
	msg['From'] = fromaddr
	msg['To'] = toaddrs
	msg['Date'] = formatdate(localtime=True)
	msg['Subject'] = subject

	# Write the body of the message
	body = 'Hello Student! \n    Thank you for using iCalCreator! Your schedule is attached! Have a great year! \n\nEnjoy! \n--iCalCreator Creators <3 \n (Byron Wasti, Keenan Zucker, Patrick Huston) \n \n \nPlease report any bugs to: \nbyron.wasti@students.olin.edu or keenan.zucker@students.olin.edu or patrick.huston@students.olin.edu'

	#attaches the multiparts to the file
	msg.attach(MIMEText(body))

	#attach the passed in file (ical)
	part = MIMEBase('application', "octet-stream")
	part.set_payload(ical.read())
	Encoders.encode_base64(part)
	part.add_header('Content-Disposition', 'attachment; filename="iCalSchedule.ics"')
	msg.attach(part)

	# Gmail Login
	username = 'iCalCreator@gmail.com'
	password = 'iCalCr3ator'

	# Sending the mail  
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.starttls()
	server.login(username,password)
	server.sendmail(fromaddr, toaddrs, msg.as_string())
	server.quit()

#test = open('OliniCalendar.ics','r')

#email = str(raw_input("Enter Email account"))
#iCalCreator(email, test)
