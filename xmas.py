#!/usr/bin/env python3
from rpi_lcd import LCD
import time
from datetime import datetime
import math
from datetime import date
import holidays

def setup():
    lcd=LCD()
    lcd.text('Greetings!!', 1)
    lcd.text(' from Don Bower', 2)
    time.sleep(2.5)

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

        lcd.text(line0message, 1)
        lcd.text(' until Christmas', 2)
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
        print(printList)

        lcd.text('Merry Christmas ', 1)
        lcd.text(printList, 2)

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
        lcd.text(line0message, 1)
        lcd.text(' until New Years', 2)
        time.sleep(.2)

def destroy():
    lcd.text('Good bye,       ', 1)
    lcd.text(' for now...     ', 2)
    pass

if __name__ == "__main__":
	try:
		setup()
		while True:
			pass
	except KeyboardInterrupt:
		destroy()
