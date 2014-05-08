#########################################################################
#                 10-row School abacus
#                         by
#                      Michael H
#########################################################################
#       Description partially extracted from from wikipedia 
#
#  Around the world, abaci have been used in pre-schools and elementary
#
# In Western countries, a bead frame similar to the Russian abacus but
# with straight wires and a vertical frame has been common (see image).
# Helps schools as an aid in teaching the numeral system and arithmetic
#
#         |00000*****   |     row factor 1000000000
#         |00000*****   |     row factor 100000000
#         |00000*****   |     row factor 10000000 
#         |00000*****   |     row factor 1000000
#         |00000*****   |     row factor 100000
#         |00000*****   |     row factor 10000
#         |00000*****   |     row factor 1000
#         |00000****   *|     row factor 100     * 1
#         |00000***   **|     row factor 10      * 2
#         |00000**   ***|     row factor 1       * 3
#                                        -----------    
#                             Sum                123 
#
# Each row represents a different row factor, starting with x1 at the
# bottom, ascending up to x1000000000 at the top row.     
######################################################################

# TASK:
# Define a procedure print_abacus(integer) that takes a positive integer
# and prints a visual representation (image) of an abacus setup for a 
# given positive integer value.
# 
# Ranking
# 1 STAR: solved the problem!
# 2 STARS: 6 < lines <= 9
# 3 STARS: 3 < lines <= 6
# 4 STARS: 0 < lines <= 3

# sketch
# if value == 0:
#     r = a * 5 + b * 5 + c * 3 + a * 0 + b * 0
# elif value == 1:
#     r = a * 5 + b * 4 + c * 3 + a * 0 + b * 1
# elif value == 2:
#     r = a * 5 + b * 3 + c * 3 + a * 0 + b * 2
# elif value == 3:
#     r = a * 5 + b * 2 + c * 3 + a * 0 + b * 3
# elif value == 4:
#     r = a * 5 + b * 1 + c * 3 + a * 0 + b * 4
# elif value == 5:
#     r = a * 5 + b * 0 + c * 3 + a * 0 + b * 5
# elif value == 6:
#     r = a * 4 + b * 0 + c * 3 + a * 1 + b * 5
# elif value == 7:
#     r = a * 3 + b * 0 + c * 3 + a * 2 + b * 5
# elif value == 8:
#     r = a * 2 + b * 0 + c * 3 + a * 3 + b * 5
# elif value == 9:
#     r = a * 1 + b * 0 + c * 3 + a * 4 + b * 5

def print_abacus(value):
       #
       ### Add you code here 
       #
    str_v = str(value)
    str_v = '0' * (10 - len(str_v)) + str_v
    a, b, c, d, e, i = '0', '*', ' ', '0', '*', 0
    while i < 10:
        value = int(str_v[i])

        _a = 10 - value
        _b = 5 - value
        _c = 3
        _d = value - 5
        _e = value

        if 0 <= value <= 5:
            _a, _d = 5, 0
        if 5 <= value <= 9:
            _b, _e = 0, 5

        r = a * _a + b * _b + c * _c + d * _d + e * _e
        print '|' + r + '|'
        i = i + 1


###  TEST CASES
print "Abacus showing 0:"
print_abacus(0)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
print "Abacus showing 12345678:"
print_abacus(12345678)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000****   *|
#>>>|00000***   **|
#>>>|00000**   ***|
#>>>|00000*   ****|
#>>>|00000   *****|
#>>>|0000   0*****|
#>>>|000   00*****|
#>>>|00   000*****|
print "Abacus showing 1337:"
print_abacus(1337)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000****   *|
#>>>|00000**   ***|
#>>>|00000**   ***|
#>>>|000   00*****|
