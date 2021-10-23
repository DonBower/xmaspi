from datetime import date
import holidays
us_holidays = holidays.UnitedStates(observed=False)

for date, name in sorted(holidays.US(years=2021).items()):
  print(date, name)

myHolidays = holidays.UnitedStates(years=[2021,2022],observed=False)

for date, name in sorted(myHolidays.items()):
  print(date, name)
