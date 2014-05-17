# Creating an Empty Hash Table
# Define a procedure, make_hashtable,
# that takes as input a number, nbuckets,
# and returns an empty hash table with
# nbuckets empty buckets.

def make_hashtable(nbuckets):
    index = []
    for e in range(0, nbuckets):
        index.append([])
    return index

print make_hashtable(2)
