import mechanize
from bs4 import BeautifulSoup
import codecs


def htmlHandle(USERNAME, PASSWORD):

	url = 'https://my.olin.edu/ICS/My_StAR/My_Schedule_and_Registration_Info.jnz'
	br = mechanize.Browser()
	br.open(url)

	br.select_form(nr=0)
	br["userName"] = USERNAME
	br["password"] = PASSWORD
	html = str(br.submit().read())

	#html = open('testhtml.html','w')
	#html.write(results)


	soup = BeautifulSoup(html)

	tabulka = soup.find(id = "pg0_V_ggCourses")
	tab = tabulka.find('tbody').findAll('tr')[0].findAll('td')[1].string

	courseNames = []
	courseTimes = []

	for row in tabulka.find('tbody').findAll('tr'):
		times = []
		course = str(row.findAll('td')[1].string.strip())
		for li in row.findAll('td')[2].findAll('li'):
			times.append(str(li.string.strip()).replace("\r\n\t\t\t\t\t\t\t\t\t\t"," "))

		courseTimes.append(times)
		courseNames.append(course)

	courseLocations = []
	for i in range(len(courseNames)):
		courseLocations.append("Location feature not yet implemented")

	numOfCourses = str(len(courseNames))
	# print courseNames
	# print courseTimes

	return [numOfCourses,courseNames,courseTimes,courseLocations]

def formatInfo(numOfCourses,courseNames,courseTimes,courseLocations):
	info = ""
	info += (numOfCourses + "\n")
	for i in range(int(numOfCourses)):
		info += (courseNames[i]+"\n")
		for j in range(len(courseTimes[i])):
			info += (str(courseTimes[i][j]) + "  ")
		info += ("\n")
		info += (courseLocations[i] + "\n")
	return info

htmlResults = htmlHandle(USERNAME,PASSWORD)

num = htmlResults[0]
names = htmlResults[1]
times = htmlResults[2]
locs = htmlResults[3]

output = formatInfo(num, names, times, locs)
print(output)