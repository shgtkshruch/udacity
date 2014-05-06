###############################################
#       Exercise by Websten from forums       #
###############################################
# A palindrome is a word or a phrase that reads 
# the same backwards as forwards. Make a program 
# that checks if a word is a palindrome. 
# If the word is a palindrome, print 0 to the terminal,
# -1 otherwise. 
# The word contains lowercase letters a-z and 
# will be at least one character long.
#
### HINT! ###
# You can read a string backwards with the following syntax:
# string[::-1] - where the "-1" means one step back.
# This exercise can be solved with only unit 1 knowledge
# (no loops or conditions)

word = "madam"
# test case 2
# word = "madman" # uncomment this to test

###
# YOUR CODE HERE. DO NOT DELETE THIS LINE OR ADD A word DEFINITION BELOW IT.
###
word_len = len(word)
center_word = word[word_len / 2]
center_position = word.find(center_word)
before = word[:center_position]
after = word[center_position + 1:]

is_palindrome = before.find(after[::-1])
print is_palindrome

# TESTING
# >>> 0  # outcome if word == "madam"
# >>> -1 # outcome if word == "madman"
