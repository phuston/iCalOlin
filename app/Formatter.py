import sys
# Setting up the program for writing the calendar files
# Starting the actual code
def formatTimes(t):
    time = []
    for i in range(len(t)):
        for j in range( len(t[i])):
            # tmp is just a temporary variable to store all the reformated code. Not very pretty, but it works
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
            
            # This can definitely be done better, but it works for the most part
            timetmp = [day]+tmp
            time.append(timetmp)
    return time

# What this code actually returns are time slots! Not time correlated to classes, which is why the timeold is needed - in order to map the classes to each time slot.

