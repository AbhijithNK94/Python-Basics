#### Generalised Matrix Multiplication #####
import numpy as np
def print_mx(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print("\t", matrix[i][j], end="")
        print("\n")
def main():
    m = int(input("Enter the number of rows of Ist Matrix: "))
    n = int(input("Enter the number of columns of Ist Matrix: "))
    p = int(input("Enter the number of rows of IInd Matrix: "))
    q = int(input("Enter the number of columns of IInd Matrix: "))
    if n != p:
        print("Matrix multiplication not possible.....")
        exit()
    array1 = [[0 for i in range(n)] for j in range(m)]
    array2 = [[0 for i in range(q)] for j in range(p)]
    result = [[0 for i in range(q)] for j in range(m)]

    print("Enter elements of Ist Matrix")
    for i in range(m):
        for j in range(n):
            array1[i][j] = int(input("Enter the element: "))
    print("Ist Matrix:-")
    print_mx(array1)
    print("Enter the elements of IInd Matrix")
    for i in range(p):
        for j in range(q):
            array2[i][j] = int(input("Enter the element: "))
    print("IInd Matrix:-")
    print_mx(array2)
    ##Multiplication
    result = np.dot(array1, array2)
    print(result)
main()