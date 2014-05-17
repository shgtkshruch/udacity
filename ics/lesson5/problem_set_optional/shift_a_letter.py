# Write a procedure, shift, which takes as its input a lowercase letter,
# a-z and returns the next letter in the alphabet after it, with 'a' 
# following 'z'.

def shift(letter):
    o = ord(letter)
    if o < 122:
        return chr(o + 1)
    else:
        return chr(97)


print shift('a')
#>>> b
print shift('n')
#>>> o
print shift('z')
#>>> a
