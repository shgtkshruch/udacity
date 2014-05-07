# Define a procedure, factorial, that
# takes one number as its input
# and returns the factorial of
# that number.

def factorial(n):
    r = 1
    while n >= 1:
        r = r * n
        n = n - 1
    return r

# test
print factorial(0)
#>>> 1 
print factorial(1)
#>>> 1 
print factorial(4)
#>>> 24
print factorial(5)
#>>> 120
print factorial(6)
#>>> 720
