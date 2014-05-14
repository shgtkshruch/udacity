# Write a procedure, convert_seconds, which takes as input a non-negative 
# number of seconds and returns a string of the form 
# '<integer> hours, <integer> minutes, <number> seconds' but
# where if <integer> is 1 for the number of hours or minutes, 
# then it should be hour/minute. Further, <number> may be an integer
# or decimal, and if it is 1, then it should be followed by second.
# You might need to use int() to turn a decimal into a float depending
# on how you code this. int(3.0) gives 3
#
# Note that English uses the plural when talking about 0 items, so
# it should be "0 minutes".
#

def str_time(num, unit):
    if num < 1:
        return '0 ' + unit + 's, '
    elif num == 1:
        return str(num) + ' ' + unit + ', '
    elif num > 1:
        return str(num) + ' ' + unit + 's, '

def convert_seconds(seconds):
    hour = int(seconds) / 60 / 60
    minute = int(seconds) / 60 - hour * 60
    second = seconds - hour * 60 ** 2 - minute * 60

    return str_time(hour, 'hour') + str_time(minute, 'minute') + str_time(second, 'second')

print convert_seconds(3661)
#>>> 1 hour, 1 minute, 1 second

print convert_seconds(7325)
#>>> 2 hours, 2 minutes, 5 seconds

print convert_seconds(7261.7)
#>>> 2 hours, 1 minute, 1.7 seconds

print convert_seconds(0)
#>>> 0 minutes

print convert_seconds(3600)
