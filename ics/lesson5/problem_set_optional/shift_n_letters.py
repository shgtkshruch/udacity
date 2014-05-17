# Write a procedure, shift_n_letters which takes as its input a lowercase
# letter, a-z, and an integer n, and returns the letter n steps in the
# alphabet after it. Note that 'a' follows 'z', and that n can be positive,
#negative or zero.

def shift_n_letters(letter, n):
    s = ord(letter) + n
    a = ord('a')
    z = ord('z')
    if s < a:
        r = z - (a - s) + 1
    elif s > z:
        r = s - 26
    else:
        r = s    
    return chr(r)


print shift_n_letters('s', 1)
#>>> t
print shift_n_letters('s', 2)
#>>> u
print shift_n_letters('s', 10)
#>>> c
print shift_n_letters('s', -10)
#>>> i
print shift_n_letters('a', -1)
#>>> z
print shift_n_letters('a', -2)
#>>> y
