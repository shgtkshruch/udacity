p = [1, 2, 3, 4, 5]

def proc1(p):
    p[0] = p[1]

def proc2(p):
    p = p + [1]

def proc3(p):
    q = p
    p.append(3)
    q.pop()

def proc4(p):
    q = []
    while p:
        q.append(p.pop())
    while q:
        p.append(q.pop())

# test

# proc1(p)
# print p 

# proc2(p)
# print p 

# proc3(p)
# print p 

# proc4(p)
# print p 
