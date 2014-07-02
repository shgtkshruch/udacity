# Double Gold Star

# Khayyam Triangle

# The French mathematician, Blaise Pascal, who built a mechanical computer in
# the 17th century, studied a pattern of numbers now commonly known in parts of
# the world as Pascal's Triangle (it was also previously studied by many Indian,
# Chinese, and Persian mathematicians, and is known by different names in other
# parts of the world).

# The pattern is shown below:

#                    1
#                   1 1
#                  1 2 1
#                 1 3 3 1
#                1 4 6 4 1
#                   ...

# Each number is the sum of the number above it to the left and the number above
# it to the right (any missing numbers are counted as 0).

# Define a procedure, triangle(n), that takes a number n as its input, and
# returns a list of the first n rows in the triangle. Each element of the
# returned list should be a list of the numbers at the corresponding row in the
# triangle.


def triangle(n):
    current, after = [], []
    for i in range(0, n):
        if i == 0:
            after.append([1])
        elif i == 1:
            after.append([1,1])
        else:
            for a in triangle(i):
                print "a"
                print a
                l = len(a)
                res = []
                for i in range(0, l-1):
                    print i
                    # res += a[i] + a[i+1]
                res = res + [1]
                res = [1] + res
            after.append(res)
        current, after = after, current + after
    return current



#For example:

# print triangle(0)
#>>> []

# print triangle(1)
#>>> [[1]]

# print triangle(2)
#>> [[1], [1, 1]]

print triangle(3)
#>>> [[1], [1, 1], [1, 2, 1]]

# print triangle(6)
#>>> [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]

