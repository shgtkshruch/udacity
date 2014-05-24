# Spreading Udaciousness
 
# One of our modest goals is to teach everyone in the world to program and
# understand computer science. To estimate how long this will take we have
# developed a (very flawed!) model:

# Everyone answering this question will convince a number, spread, (input to 
# the model) of their friends to take the course next offering. This will 
# continue, so that all of the newly recruited students, as well as the original
# students, will convince spread of their
# friends to take the following offering of the course.
# recruited friends are unique, so there is no duplication among the newly
# recruited students. Define a procedure, hexes_to_udaciousness(n, spread,
# target), that takes three inputs: the starting number of Udacians, the spread
# rate (how many new friends each Udacian convinces to join each hexamester),
# and the target number, and outputs the number of hexamesters needed to reach 
# (or exceed) the target.

# For credit, your procedure must not use: while, for, or import math. 

# while loop
def hexes_to_udaciousness(n, spread, target):
    target_new_user = target - n
    get_new_user = n * spread
    res = 0
    if target_new_user < 0:
        return 0
    while target_new_user >= get_new_user:
        now_user = n + get_new_user
        get_new_user += now_user * spread
        res += 1
    if target_new_user % get_new_user:
        res += 1
    return 1

# recursive
def hexes_to_udaciousness(n, spread, target):
    target_new_user = target - n
    get_new_user = n * spread
    loop_num = 0
    if target_new_user < 0:
        return loop_num
    else:
        if target_new_user > get_new_user:
            now_user = n + get_new_user
            get_new_user += now_user * spread
            loop_num += hexes_to_udaciousness(now_user, spread, target)
        return loop_num + 1

# anser
def hexes_to_udaciousness(n, spread, target):
    if n >= target:
        return 0
    else:
        return 1 + hexes_to_udaciousness(n * (1 + spread), spread, target)

# n += hexes_to_udaciousness() => 1 or 0

# 0 more needed, since n already exceeds target
print hexes_to_udaciousness(100000, 2, 36230) 
#>>> 0

# after 1 hexamester, there will be 50000 + (50000 * 2) Udacians
print hexes_to_udaciousness(50000, 2, 150000) 
#>>> 1 

# need to match or exceed the target
print hexes_to_udaciousness(50000, 2, 150001)
#>>> 2 

# only 12 hexamesters (2 years) to world domination!
print hexes_to_udaciousness(20000, 2, 7 * 10 ** 9) 
#>>> 12 

# more friends means faster world domination!
print hexes_to_udaciousness(15000, 3, 7 * 10 ** 9)
#>>> 10 



