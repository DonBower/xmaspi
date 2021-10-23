from datetime import date
import holidays
us_holidays = holidays.UnitedStates(observed=False)

# myHolidays = holidays.UnitedStates(years=[2021,2022],observed=False)
myHolidays = us_holidays(years=[2021,2022])
myHolidays.pop_named("Martin Luther King")
myHolidays.pop_named("Washington")
myHolidays.pop_named("Columbus Day")
myHolidays.pop_named("Memorial")
myHolidays.pop_named("Juneteenth")
myHolidays.pop_named("Independence")
myHolidays.pop_named("Labor")
myHolidays.pop_named("Veterans")
myHolidays[date(2021, 7, 13)] = "Ninja Turtle Day"


for date, name in sorted(myHolidays.items()):
  print(date, name)



# 2021-01-01 New Year's Day
# 2021-01-18 Martin Luther King Jr. Day
# 2021-02-15 Washington's Birthday
# 2021-05-31 Memorial Day
# 2021-06-19 Juneteenth National Independence Day
# 2021-07-04 Independence Day
# 2021-07-05 Independence Day (Observed)
# 2021-09-06 Labor Day
# 2021-10-11 Columbus Day
# 2021-11-11 Veterans Day
