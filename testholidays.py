from datetime import date
import holidays
us_holidays = holidays.UnitedStates()

for date, name in sorted(holidays.US(years=2021).items()):
  print(date, name)