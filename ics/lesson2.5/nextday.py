###
### Define a simple nextDay procedure, that assumes
### every month has 30 days.
###
### For example:
###    nextDay(1999, 12, 30) => (2000, 1, 1)
###    nextDay(2013, 1, 30) => (2013, 2, 1)
###    nextDay(2012, 12, 30) => (2013, 1, 1)  (even though December really has 31 days)
###

# my code
def nextDay(year, month, day):
    """
    Returns the year, month, day of the next day.
    Simple version: assume every month has 30 days.
    """
    # YOUR CODE HERE
    n_year = year
    n_month = month
    n_day = day + 1
    if n_day > 30:
        n_day = 1
        n_month = month + 1
    if n_month > 12:
        n_month = 1
        n_year = year + 1

    return n_year, n_month, n_day

# Answer
def nextDay(year, month, day):
    if day < 30:
        return year, month, day + 1
    else:
        if month < 12:
            return year, month + 1, 1
        else:
            return year + 1, 1, 1
         

print nextDay(1999, 12, 30) # => (2000, 1, 1)
print nextDay(2013, 1, 30) # => (2013, 2, 1)
print nextDay(2012, 12, 30) # => (2013, 1, 1)
