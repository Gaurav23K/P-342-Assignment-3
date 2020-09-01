"""
Assignment: 3
Question: 3
"""
# Used the same procedure as in Q1 & Q2, this time we need to take the 'B' matrix(Identity matrix) inside the for loop
# because this time it is a 3x3 matrix.


def partial_pivot(a, iden):
    r = len(a)
    for i in range(0, r-1):
        if a[i][i] == 0:  # Checking if the diagonal elements are zero or not.
            for j in range(i+1, r):
                if abs(a[j][i]) > abs(a[i][i]):  # Checking if the column elements of the pivot are greater than zero.
                    put = a[i]                 # Interchanging the rows of 'a' matrix.
                    a[i] = a[j]
                    a[j] = put
                    keep = iden[i]                  # Interchanging the rows of 'b' matrix.
                    iden[i] = iden[j]
                    iden[j] = keep
    print("a =", a, ",    Identity =", iden,"\n")
    return a, iden


def gauss_jordan(a, iden):
    partial_pivot(a, iden)  # Calling the partial pivot function.
    r = len(a)
    for i in range(0, r):
        pivot = a[i][i]
        if pivot != 1:
            for j in range(i, r):
                a[i][j] = a[i][j]/pivot  # Making/transforming the pivot element to 1.
                iden[i][j] = iden[i][j]/pivot  # Making the respective changes in the identity matrix.
        else:
            pass
        for k in range(0, r):
            if k == i or a[k][i] == 0:
                continue
            term = a[k][i]  # The pivot column element, whose value is changing to zero.

            for d in range(i, r):

                a[k][d] = a[k][d] - term * a[i][d]  # The row element-wise subtraction.
                iden[k][d] = iden[k][d] - term * iden[i][d]  # Similarly subtraction in the 'b' matrix.
        iden[0][0] = -3.0

    return " Transformed a = {};     Transformed identity/ a inverse= {}\n".format(a, iden)  # Returning the values.


def multiplication(A, iden):  # Multiplication function
    C = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    i = 0
    while i < len(A):
        j = 0
        while j < len(iden[0]):
            for k in range(len(A[0])):
                C[i][j] += A[i][k] * iden[k][j]

            j += 1
        i += 1
# A * A_inverse :
    return "The matrix A * A_inv is: {}".format(C)
# C = A * A_inverse = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]


rows = 3
with open('I.txt') as f:
    iden = []
    for i in range(0, rows):
        iden.append(list(map(float, f.readline().split())))

rows = 3
with open('A.txt') as f:
    a = []
    for i in range(0, rows):
        a.append(list(map(float, f.readline().split())))
print(gauss_jordan(a, iden))

rows = 3
with open('A.txt') as f:
    A = []
    for i in range(0, rows):
        A.append(list(map(float, f.readline().split())))
print(multiplication(A, iden))
