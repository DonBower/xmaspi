from datetime import date, time
import datetime
import math
from time import sleep
import holidays

now = datetime.datetime.now()
thisYear = now.year
nextYear = thisYear + 1
midnight = datetime.datetime.time
sleepTime = 2

easterDates = {}
easterDates["2021"] = [4,4]
easterDates["2022"] = [4,17]
easterDates["2023"] = [4,9]
easterDates["2024"] = [3,31]
easterDates["2025"] = [4,20]
easterDates["2026"] = [4,5]
easterDates["2027"] = [3,28]
easterDates["2028"] = [4,16]
easterDates["2029"] = [4,1]
easterDates["2030"] = [4,21]
easterDates["2031"] = [4,13]
easterDates["2032"] = [3,28]

myHolidays = holidays.UnitedStates(years=[thisYear,nextYear],observed=False)
nextEaster = easterDates[str(nextYear)]
myHolidays.pop_named("Martin Luther King")
myHolidays.pop_named("Washington")
myHolidays.pop_named("Columbus Day")
myHolidays.pop_named("Memorial")
myHolidays.pop_named("Juneteenth")
myHolidays.pop_named("Independence")
myHolidays.pop_named("Labor")
myHolidays.pop_named("Veterans")
# print("Remove thisNewYears")
# print(date(thisYear,1,1))

myHolidays.pop(datetime.date(thisYear, 1,  1))
myHolidays[datetime.date(thisYear, 10,  31)] = "Halloween" 
myHolidays[datetime.date(nextYear, nextEaster[0], nextEaster[1])] = "Easter"
myHolidays[datetime.date(nextYear, 2,  14)] = "St. Valentine's Day"
myHolidays[datetime.date(thisYear, 10,  26)] = "Test Day"

def getFutureTime(thisHolidayDate):
  thisMoment = datetime.datetime.now()
  holidayDateTime = datetime.datetime(thisHolidayDate.year, thisHolidayDate.month, thisHolidayDate.day) 
  timeDifference = holidayDateTime - thisMoment
  return timeDifference

for thisHolidayDate, thisHolidayName in sorted(myHolidays.items()):
  print(thisHolidayDate, thisHolidayName)

for thisHolidayDate, thisHolidayName in sorted(myHolidays.items()):
  getFutureTime(thisHolidayDate)
  futureTime = getFutureTime(thisHolidayDate)

  futureDays = int(futureTime.days)

  while futureDays > 0:
    if futureDays < 100:
      futureSeconds = futureTime.seconds
      futureHours = int(math.floor(futureSeconds / 3600))
      futureMinutes = int(math.floor((futureSeconds - (futureHours * 3600)) / 60))
      futureSeconds = futureSeconds - (futureHours * 3600) - (futureMinutes * 60)
      line0String = str(futureDays) + " Days, " + f"{futureHours:02d}" + ":" + f"{futureMinutes:02d}" + ":" + f"{futureSeconds:02d}"
    else:
      line0String = str(futureDays) + " Days "
    line1String = "Until " + thisHolidayName
    print(line0String)
    print(line1String)
    sleep(sleepTime)
    futureTime = getFutureTime(thisHolidayDate)

  while futureDays == 0:
    futureSeconds = futureTime.seconds
    futureHours = int(math.floor(futureSeconds / 3600))
    futureMinutes = int(math.floor((futureSeconds - (futureHours * 3600)) / 60))
    futureSeconds = futureSeconds - (futureHours * 3600) - (futureMinutes * 60)
    line0String = f"{futureHours:1d}" + " hours, " + f"{futureMinutes:02d}" + ":" + f"{futureSeconds:02d}"
    line1String = "Until " + thisHolidayName
    print(line0String)
    print(line1String)
    sleep(sleepTime)
    futureTime = getFutureTime(thisHolidayDate)
