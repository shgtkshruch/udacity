# Given a variable, x, that stores the 
# value of any decimal number, write Python 
# code that prints out the nearest whole 
# number to x.
# If x is exactly half way between two 
# whole numbers, round up, so
# 3.5 rounds to 4 and 2.5 rounds to 3.
# You may assume x is not negative.

# Hint: The str function can convert any number into a string.
# eg str(89) converts the number 89 to the string '89'

# Along with the str function, this problem can be solved 
# using just the information introduced in unit 1.

# x = 3.14159 
# >>> 3 (not 3.0)
# x = 27.63 
# >>> 28 (not 28.0)
# x = 3.5 
# >>> 4 (not 4.0)

x = 3.14159
x = 27.63 
x = 3.5 

#ENTER CODE BELOW HERE
def round_up(x):
    round_up = x  + .5
    str_x = str(round_up)
    point = str_x.find('.')
    before_point = str_x[:point]
    return before_point

# test
x = 3.14159
print '3' == round_up(x)

x = 27.63 
print '28' == round_up(x)

x = 3.5 
print '4' == round_up(x)
