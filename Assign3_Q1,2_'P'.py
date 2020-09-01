"""
Assignment: 3
Question: 1 & 2
"""


def partial_pivot(a, b):
    r = len(a)
    for i in range(0, r-1):
        if a[i][i] == 0:  # Checking if the diagonal elements are zero or not.
            for j in range(i+1, r):
                if abs(a[j][i]) > abs(a[i][i]):  # Checking if the column elements of the pivot are greater than zero.
                    put = a[i]                 # Interchanging the rows of 'a' matrix.
                    a[i] = a[j]
                    a[j] = put
                    keep = b[i]                  # Interchanging the rows of 'b' matrix.
                    b[i] = b[j]
                    b[j] = keep
    print("a =", a, ",    b =", b)
    return a, b


def gauss_jordan(a, b):
    partial_pivot(a, b)  # Calling the partial pivot function.
    r = len(a)
    for i in range(0, r):
        pivot = a[i][i]
        if pivot != 1:
            for j in range(i, r):
                a[i][j] = a[i][j]/pivot  # Making/transforming the pivot element to 1.
            b[i] = b[i]/pivot
        else:
            pass
        for k in range(0, r):
            if k == i or a[k][i] == 0:
                continue
            term = a[k][i]  # The pivot column element, whose value is changing to zero.
            for d in range(i, r):
                a[k][d] = a[k][d] - term * a[i][d]  # The row element-wise subtraction.
            b[k] = b[k] - term * b[i]  # Similarly subtraction in the 'b' matrix/vector.
    return " Transformed a = {};     Transformed b= {}".format(a, b)  # Returning the values.


"""
Q1). b == [3, 1, -2]
Q2). b == [-2, -2, 1]
"""

# print(gauss_jordan([[0, 2, 5], [3, -1, 2], [1, -1, 3]], [1, -2, 3]))
# print(gauss_jordan([[1, 3, 2], [2, 7, 7], [2, 5, 2]], [2, -1, 7]))

vec = open('b1.txt', 'r')
split = vec.readline().split()
b = []
for i in split:
    b.append(float(i))

rows = 3
with open('a1.txt') as f:
    a = []
    for i in range(0, rows):
        a.append(list(map(float, f.readline().split())))

print(gauss_jordan(a, b))

vec = open('b2.txt', 'r')
split = vec.readline().split()
b = []
for i in split:
    b.append(float(i))

rows = 3
with open('a2.txt') as f:
    a = []
    for i in range(0, rows):
        a.append(list(map(float, f.readline().split())))

print(gauss_jordan(a, b))
