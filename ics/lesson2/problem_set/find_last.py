# Define a procedure, find_last, that takes as input
# two strings, a search string and a target string,
# and returns the last position in the search string
# where the target string appears, or -1 if there
# are no occurences.
#
# Example: find_last('aaaa', 'a') returns 3

# Make sure your procedure has a return statement.

# my code
def find_last(string, target):
    if string == '' and target == '':
        return 0
    if string == '':
        return -1

    if len(string) < len(target):
        string, target = target, string

    pos = string.find(target)
    result = -1

    while pos != -1:
        result = pos
        pos = string.find(target, pos + 1)
        if pos == -1:
            return result
        result = pos

    return result

# answer
def find_last(s, t):
    last_pos = -1
    while True:
        pos = s.find(t, last_pos + 1)
        if pos == -1:
            return last_pos
        last_pos = pos

print find_last('aaaa', 'a')
# #>>> 3
#
print find_last('aaaaa', 'aa')
# #>>> 3
#
print find_last('aaaa', 'b')
# #>>> -1
#
print find_last("111111111", "1")
# #>>> 8
#
print find_last("222222222", "")
# #>>> 9
#
print find_last("", "3")
# #>>> -1
#
print find_last("3", "")
# #>>> 1
#
print find_last("", "")
# #>>> 0
#
print find_last('dab', 'ccabccdddbcbacadaddabbbdddaacb')
# #>>> 18
#
