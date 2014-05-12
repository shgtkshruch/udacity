# Define a procedure, add_to_index,
# that takes 3 inputs:

# - an index: [[<keyword>,[<url>,...]],...]
# - a keyword: String
# - a url: String

# If the keyword is already
# in the index, add the url
# to the list of urls associated
# with that keyword.

# If the keyword is not in the index,
# add an entry to the index: [keyword,[url]]

index = []

def keyword_index(entry):
    r = []
    for e in entry:
        r.append(e[0])
    return r

def is_not_index(index, keyword):
    for e in index:
        if e == keyword:
            return False
    return True

def add_to_index(index,keyword,url):
    i = keyword_index(index)
    if is_not_index(i, keyword):
        index.append([keyword, [url]])
    else:
        index[i.index(keyword)][1].append(url)


add_to_index(index,'udacity','http://udacity.com')
add_to_index(index,'computing','http://acm.org')
add_to_index(index,'udacity','http://npr.org')
print index
#>>> [['udacity', ['http://udacity.com', 'http://npr.org']], 
#>>> ['computing', ['http://acm.org']]]



