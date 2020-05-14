from datetime import datetime

def timediff(time1, time2):
    timea = datetime.strptime(time1, "%H:%M")
    timeb = datetime.strptime(time2, "%H:%M")
    if timea >= timeb:
        newtime = timea - timeb
        return int(newtime.seconds / 60)
    else:
        newtime = timea - timeb
        return int(-newtime.seconds / 60)


def getclosest(lst, K):
    num = lst[min(range(len(lst)), key=lambda i: abs(lst[i] - K))]
    return num

input1 = "5,8,10:30,11:30"  
#Input 5 team members, located on the 8th floor, meeting time 10:30 - 11:30 
ipcapacity, ipfloor, ipstart, ipend = input1.split(",")
#print("ipcapacity:" + ipcapacity + "\nipfloor:" + ipfloor + "\nipstart:" + ipstart + "\nipend:" + ipend)
availablerooms = []

file1 = open('rooms.txt', 'r')
while True:
    # Read next line from file
    line = file1.readline()

    # if line is empty
    # end of file is reached
    if not line:
        break
    #strip the line for all white space etc and split it with comma
    x = line.strip().split(",")
    #further the first string from above split to get floor and room details 
    floor = x[0].split('.')[0]
    room = x[0].split('.')[1]
    capacity = x[1]
    #check the capacity of meeting room
    if capacity >= ipcapacity:
        for i in range(2, len(x), 2):
            #check the starting time and its availability 
            checkStarttime = timediff(ipstart, x[i])
            if checkStarttime >= 0:
                checkEndtime = timediff(x[i + 1], ipend)
                # check meeting end time availability if starting time available as per the duration of meeting
                if checkEndtime >= 0:
                    #collect info for all available meeting room 
                    availablerooms.append(x[0])


file1.close()
if not availablerooms:
    #if no room is available as per the requirement 
    print("Sorry, no meeting available to meet your requirement")
else:
#   converting list of available meeting rooms into dict
    floorrooms = {int(fr.split('.')[0]): int(fr.split('.')[1]) for fr in availablerooms}
#   sorting the dict on floor and picking the closest floor
#   same logic could be use to get the nearest meeting room in case needed
    closestfloor = getclosest(sorted(floorrooms), int(ipfloor))
    print("{0}.{1}".format(closestfloor, floorrooms[closestfloor]))
