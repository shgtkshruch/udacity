# Write a procedure download_time which takes as inputs a file size, the
# units that file size is given in, bandwidth and the units for
# bandwidth (excluding per second) and returns the time taken to download 
# the file.
# Your answer should be a string in the form
# "<number> hours, <number> minutes, <number> seconds"

# Some information you might find useful is the number of bits
# in kilobits (kb), kilobytes (kB), megabits (Mb), megabytes (MB),
# gigabits (Gb), gigabytes (GB) and terabits (Tb), terabytes (TB).

#print 2 ** 10      # one kilobit, kb
#print 2 ** 10 * 8  # one kilobyte, kB

#print 2 ** 20      # one megabit, Mb
#print 2 ** 20 * 8  # one megabyte, MB

#print 2 ** 30      # one gigabit, Gb
#print 2 ** 30 * 8  # one gigabyte, GB

#print 2 ** 40      # one terabit, Tb
#print 2 ** 40 * 8  # one terabyte, TB

# Often bandwidth is given in megabits (Mb) per second whereas file size 
# is given in megabytes (MB).

def str_time(num, unit):
    if num < 1:
        return str(num) + ' ' + unit + 's, '
    elif num == 1:
        return str(num) + ' ' + unit + ', '
    elif num > 1:
        return str(num) + ' ' + unit + 's, '

def convert_seconds(seconds):
    hour = int(seconds) / 60 / 60
    minute = int(seconds) / 60 - hour * 60
    second = seconds - hour * 60 ** 2 - minute * 60

    return str_time(hour, 'hour') + str_time(minute, 'minute') + str_time(second, 'second')

def convert_kb(size, unit):
    if unit == 'kb':
        return size * 2. ** 10      # one kilobit, kb
    elif unit == 'kB':
        return size * 2. ** 10 * 8  # one kilobyte, kB
    elif unit == 'Mb':
        return size * 2. ** 20      # one megabit, Mb
    elif unit == 'MB':
        return size * 2. ** 20 * 8  # one megabyte, MB
    elif unit == 'Gb':
        return size * 2. ** 30      # one gigabit, Gb
    elif unit == 'GB':
        return size * 2. ** 30 * 8  # one gigabyte, GB
    elif unit == 'Tb':
        return size * 2. ** 40      # one terabit, Tb
    elif unit == 'TB':
        return size * 2. ** 40 * 8  # one terabyte, TB

def download_time(size, f_unit, band, b_unit):
    seconds = convert_kb(size, f_unit) / convert_kb(band, b_unit)
    return convert_seconds(seconds)

print download_time(1024,'kB', 1, 'MB')
#>>> 0 hours, 0 minutes, 1 second

print download_time(1024,'kB', 1, 'Mb')
#>>> 0 hours, 0 minutes, 8 seconds  # 8.0 seconds is also acceptable

print download_time(13,'GB', 5.6, 'MB')
#>>> 0 hours, 39 minutes, 37.1428571429 seconds

print download_time(13,'GB', 5.6, 'Mb')
#>>> 5 hours, 16 minutes, 57.1428571429 seconds

print download_time(10,'MB', 2, 'kB')
#>>> 1 hour, 25 minutes, 20 seconds  # 20.0 seconds is also acceptable

print download_time(10,'MB', 2, 'kb')
#>>> 11 hours, 22 minutes, 40 seconds  # 40.0 seconds is also acceptable



