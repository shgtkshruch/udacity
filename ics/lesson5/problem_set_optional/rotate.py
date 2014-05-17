# Write a procedure, rotate which takes as its input a string of lower case
# letters, a-z, and spaces, and an integer n, and returns the string constructed
# by shifting each of the letters n steps, and leaving the spaces unchanged.
# Note that 'a' follows 'z'. You can use an additional procedure if you
# choose to as long as rotate returns the correct string.
# Note that n can be positive, negative or zero.

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

def rotate(letters, n):
    # Your code here
    res = ''
    for letter in letters:
        res += ' ' if letter == ' ' else shift_n_letters(letter, n)
    return res

print rotate ('sarah', 13)
#>>> 'fnenu'
print rotate('fnenu',13)
#>>> 'sarah'
print rotate('dave',5)
#>>>'ifaj'
print rotate('ifaj',-5)
#>>>'dave'
print rotate(("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu "
                "sv rscv kf ivru kyzj"),-17)
#>>> ???
