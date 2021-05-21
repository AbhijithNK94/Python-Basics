# Finding the determinant of a matrix #####

# Skeleton of the program

A = [[-1, 2, 1],
     [0, 2, 5],
     [3, 6, 2]]


sub_matrix = A.copy()[1:]
print(sub_matrix[0][0:0] + sub_matrix[0][1:])
print(sub_matrix[1][0:0] + sub_matrix[1][1:])
print(sub_matrix[0][0:1] + sub_matrix[0][2:])
print(sub_matrix[1][0:1] + sub_matrix[1][2:])
print(sub_matrix[0][0:2] + sub_matrix[0][3:])
print(sub_matrix[1][0:2] + sub_matrix[1][3:])

def det(matrix):
    return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])


s = 0
for j in range(len(A)):
    sub_matrix = A.copy()[1:]
    for i in range(len(sub_matrix)):
        print(i, j, j+1)
        sub_matrix[i] = sub_matrix[i][0:j] + sub_matrix[i][j+1:]
    s += ((-1)**j) * A[0][j] * det(sub_matrix)
    print(sub_matrix)
    print(det(sub_matrix))
    print(s)

# As a standard function:


def det(matrix, total = 0):
    if len(matrix) == 2 and len(matrix[0]) == 2:
        return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
    for j in range(len(matrix)):
        sub_matrix = matrix[1:]
        for i in range(len(sub_matrix)):
            sub_matrix[i] = sub_matrix[i][0:j] + sub_matrix[i][j+1:]
        total += ((-1)**j) * det(sub_matrix) * matrix[0][j]
    return total


print(det(A))





