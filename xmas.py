#!/usr/bin/env python
import LCD1602
import time
from datetime import datetime
import math


def setup():
    LCD1602.init(0x27, 1)	# init(slave address, background light)
    LCD1602.write(0, 0, 'Greetings!!')
    LCD1602.write(1, 1, 'from Don Bower')
    time.sleep(.5)

    now = datetime.now()
    thisYear = now.year
    nextYear = thisYear + 1
    christmas = datetime.strptime("12/25/" + str(thisYear), "%m/%d/%Y")
    christmasplusone = datetime.strptime("12/25/" + str(thisYear), "%m/%d/%Y")
    newyears = datetime.strptime("12/25/" + str(nextYear), "%m/%d/%Y")
    print(now)
    print(christmas)
    print(newyears)
    while (now < christmas):
        now = datetime.now()
        diff = christmas - now
        days = diff.days
        seconds = int(diff.seconds)
        hours = int(math.floor(seconds / 3600))
        minutes = int(math.floor((seconds - (hours * 3600)) / 60))
        secs = seconds - (hours * 3600) - (minutes * 60)
        strHours = str(hours)
        strMinutes = str(minutes)
        strSeconds = str(secs)

        if secs < 10:
            strSeconds = "0" + strSeconds
        if minutes < 10:
            strMinutes = "0" + strMinutes
        if hours < 10:
            strHours = " " + strHours

        line0message = str(days) + " Days " + strHours + ":" + strMinutes + ":" + strSeconds

        if days > 99:
            line0message = str(days) + " Days "

        LCD1602.write(0, 0, line0message)
        LCD1602.write(1, 1, 'until Christmas')
        time.sleep(.2)

    thisGuestNumber = 0
    guestList = ["Don", "Sandy", "Erica", "Hector", "Julian", "Alexandra"]

    while (now < christmasplusone):
        now = datetime.now()
        diff = christmas - now
        days = diff.days
        seconds = int(diff.seconds)
        hours = int(math.floor(seconds / 3600))
        minutes = int(math.floor((seconds - (hours * 3600)) / 60))
        secs = seconds - (hours * 3600) - (minutes * 60)
        strHours = str(hours)
        strMinutes = str(minutes)
        strSeconds = str(secs)

        if secs < 10:
            strSeconds = "0" + strSeconds
        if minutes < 10:
            strMinutes = "0" + strMinutes
        if hours < 10:
            strHours = " " + strHours

        thisGuest = guestList[thisGuestNumber]
        nameLenght = len(thisGuest)
        nameOffset = (16 - nameLenght) / 2
        printList = ' ' * nameOffset + thisGuest + '                '
        printList = printList[:16]
        print printList

        LCD1602.write(0, 0, 'Merry Christmas ')
        LCD1602.write(1, 1, printList)

        thisGuestNumber = thisGuestNumber + 1

        if thisGuestNumber >= len(guestList):
          thisGuestNumber = 0

        time.sleep(2)

    while (now < newyears):
        now = datetime.now()
        diff = christmas - now
        days = diff.days
        seconds = int(diff.seconds)
        hours = int(math.floor(seconds / 3600))
        minutes = int(math.floor((seconds - (hours * 3600)) / 60))
        secs = seconds - (hours * 3600) - (minutes * 60)
        strHours = str(hours)
        strMinutes = str(minutes)
        strSeconds = str(secs)

        if secs < 10:
            strSeconds = "0" + strSeconds
        if minutes < 10:
            strMinutes = "0" + strMinutes
        if hours < 10:
            strHours = " " + strHours

        line0message = str(days) + " Days " + strHours + ":" + strMinutes + ":" + strSeconds
        LCD1602.write(0, 0, line0message)
        LCD1602.write(1, 1, 'until New Years')
        time.sleep(.2)

def destroy():
    LCD1602.write(0, 0, 'Good bye,       ')
    LCD1602.write(1, 1, 'for now...      ')
    pass

if __name__ == "__main__":
	try:
		setup()
		while True:
			pass
	except KeyboardInterrupt:
		destroy()
