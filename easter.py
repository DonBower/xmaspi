#!/usr/bin/python

def calcEasterDate(year):
    """
    Use easter date algorithm to calculate the day of
    easter for a given year.
    
    If the year given is in a special range(special_years)
    then subtract 7 from the final date.
    
    Return the date to the user.
    """
    
    special_years = ['1954', '1981', '2049', '2076']
    specyr_sub = 7
    a = year % 19
    b = year % 4
    c = year % 7
    d = (19 * a + 24) % 30
    e = ((2 * b) + (4 * c) + (6 * d) + 5) % 7
  
    if year in special_years:
        dateofeaster = (22 + d + e) - specyr_sub
    else:
        dateofeaster = 22 + d + e
    return dateofeaster


def main():
    year = int(input("Please enter a year: "))

    if (year >= 1900) and (year <= 2099):
        dateofeaster = calcEasterDate(year)
        if dateofeaster > 31:
            print("April {}".format(dateofeaster - 31))
        else:
            print("March {}".format(dateofeaster))
    else:
        print("Error: Year is out of range: 1900 - 2099")


if __name__ == main():
    main()