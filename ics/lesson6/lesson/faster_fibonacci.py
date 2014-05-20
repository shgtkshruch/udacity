#Define a faster fibonacci procedure that will enable us to computer
#fibonacci(36).

# my code
def fibonacci(n):
    i, fib, fib_0, fib_1 = 0, 0, 0, 1
    while i <= n:
        if i == 0:
            fib += fib_0
        elif i == 1:
            fib += fib_1
        else:
            fib = fib_0 + fib_1
            fib_0, fib_1 = fib_1, fib
        i += 1
    return fib

# answer
def fibonacci(n):
    current, after = 0, 1
    for i in range(0, n):
        current, after = after, current + after
    return current

print fibonacci(36)
#>>> 14930352
