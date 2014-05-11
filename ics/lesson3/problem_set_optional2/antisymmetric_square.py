# By Dimitris_GR from forums
# Modify Problem Set 31's (Optional) Symmetric Square to return True 
# if the given square is antisymmetric and False otherwise. 
# An nxn square is called antisymmetric if A[i][j]=-A[j][i] 
# for each i=0,1,...,n-1 and for each j=0,1,...,n-1.

def row(p, n):
    return p[n]

def column(p, n):
    col = []
    i = 0
    while i < len(p):
        col.append(p[i][n])
        i += 1
    return col

def antisymmetric(A):
    #Write your code here
    i = 0
    while i < len(A):
        r = row(A, i)
        c = column(A, i)
        j = 0
        while j < len(r):
            if r[j] != c[j] * -1:
                return False 
            j += 1
        i += 1
    return True


# Test Cases:

print antisymmetric([[0, 1, 2], 
                     [-1, 0, 3], 
                     [-2, -3, 0]])   
#>>> True

print antisymmetric([[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]])
#>>> True

print antisymmetric([[0, 1, 2], 
                     [-1, 0, -2], 
                     [2, 2,  3]])
#>>> False

print antisymmetric([[1, 2, 5],
                     [0, 1, -9],
                     [0, 0, 1]])
#>>> False

