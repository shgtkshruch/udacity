# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#

def days_of_months(year):
    common = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # 365
    leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # 366
    if year % 4 != 0:
        return common
    elif year % 100 != 0:
        return leap
    elif year % 400 != 0:
        return common
    else:
        return leap

def days(year, month, day):
    y = 1
    m = 1
    d = 1
    days = 0
    while y < year:
        daysOfMonths = days_of_months(y)
        i = 1
        while i <= 12:
            days = days + daysOfMonths[i - 1]
            i = i + 1
        y = y + 1

    daysOfMonths = days_of_months(year)
    while m < month:
        days = days + daysOfMonths[m - 1]
        m = m + 1

    return days + day - d

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    ##
    # Your code here.
    ##
    return days(year2, month2, day2) - days(year1, month1, day1)

# daysBetweenDates(2014,1,1,2012,2,28)
# daysBetweenDates(2012,1,1,2012,3,1)
# daysBetweenDates(2011,6,30,2012,6,30)

# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()

