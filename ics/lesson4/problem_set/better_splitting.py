# 1 Gold Star

# The built-in <string>.split() procedure works
# okay, but fails to find all the words on a page
# because it only uses whitespace to split the
# string. To do better, we should also use punctuation
# marks to split the page into words.

# Define a procedure, split_string, that takes two
# inputs: the string to split and a string containing
# all of the characters considered separators. The
# procedure should return a list of strings that break
# the source string up by the characters in the
# splitlist.

# my code
def my_split(string, split):
    r = []
    for e in string.split(split):
        r.append(e)
    return to_s(r)

def to_s(l):
    s = ''
    for e in l:
        s += e + 'separate'
    return s

def split_string(source,splitlist):
    r = []
    for sp in splitlist:
        source = my_split(source, sp)
    for e in source.split('separate'):
        if not e == '':
            r.append(e)
    return r

# answer
def split_string(source, splitlist):
    output = []
    atsplit = True
    for char in source:
        if char in splitlist:
            atsplit = True
        else:
            if atsplit:
                output.append(char)
                atsplit = False
            else:
                output[-1] += char
    return output

a = ['a']
c = ['c']
a.append('b')
c[-1] += 'b'
print a
print c

# out = split_string("This is a test-of the,string separation-code!"," ,!-")
# print out
#>>> ['This', 'is', 'a', 'test', 'of', 'the', 'string', 'separation', 'code']

# out = split_string("After  the flood   ...  all the colors came out.", " .")
# print out
#>>> ['After', 'the', 'flood', 'all', 'the', 'colors', 'came', 'out']

# out = split_string("First Name,Last Name,Street Address,City,State,Zip Code",",")
# print out
#>>>['First Name', 'Last Name', 'Street Address', 'City', 'State', 'Zip Code']
