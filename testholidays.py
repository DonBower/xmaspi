from datetime import date
import holidays

myHolidays = holidays.UnitedStates(years=[2021,2022],observed=False)
myHolidays.pop_named("Martin Luther King")
myHolidays.pop_named("Washington")
myHolidays.pop_named("Columbus Day")
myHolidays.pop_named("Memorial")
myHolidays.pop_named("Juneteenth")
myHolidays.pop_named("Independence")
myHolidays.pop_named("Labor")
myHolidays.pop_named("Veterans")
myHolidays[date(2021, 7, 13)] = "Ninja Turtle Day"
myHolidays[date(2022, 4, 17)] = "Easter" 
myHolidays[date(2023, 4,  9)] = "Easter" 
myHolidays[date(2024, 3, 31)] = "Easter" 
myHolidays[date(2025, 4, 20)] = "Easter" 
myHolidays[date(2026, 4,  5)] = "Easter" 
myHolidays[date(2027, 3, 28)] = "Easter" 
myHolidays[date(2028, 4, 16)] = "Easter" 
myHolidays[date(2029, 4,  1)] = "Easter" 
myHolidays[date(2030, 4, 21)] = "Easter" 
myHolidays[date(2031, 4, 13)] = "Easter" 
myHolidays[date(2032, 3, 28)] = "Easter" 


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
