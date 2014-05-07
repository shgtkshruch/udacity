# Define a procedure, print_numbers, that takes
# as input a positive whole number, and prints 
# out all the whole numbers from 1 to the input
# number.

# Make sure your procedure prints "upwards", so
# from 1 up to the input number.

def print_numbers(number):
    i = 0
    while i < number:
        i = i + 1
        print i

print_numbers(3)
#>>> 1
#>>> 2
#>>> 3
