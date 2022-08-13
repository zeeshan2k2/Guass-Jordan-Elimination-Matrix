# python program for gauss-jordan method in a 3*3 matrix
# function to print list in a matrix form
def printmatrix():
    for i in matrix:
        for j in i:
            print(j, end="  ")
        print()


# function to solve the pivot column
def pivotelement():
    rows = int(input("Enter the number of rows:"))
    rows -= 1
    colm = int(input("Enter the number of columns:"))
    colm -= 1
    # for first row pivot element
    pivot_element = matrix[rows][colm]
    print()
    print(pivot_element, "is pivot element")
    print()
    # divide pivot element by pivot row
    for i in range(len(matrix)):
        matrix[rows][i] = matrix[rows][i] / pivot_element
    for row in range(len(matrix)):
        if row == rows:
            continue
        else:
            make_zero = matrix[row][colm]
            for col in range(len(matrix)):
                matrix[row][col] = matrix[row][col] - make_zero * matrix[rows][col]


# row number 1
list1 = []
print("Enter numbers for first row")
for i in range(3):
    data = int(input())
    list1.append(data)
# row number 2
list2 = []
print("Enter numbers for second row")
for i in range(3):
    data = int(input())
    list2.append(data)
# row number 3
list3 = []
print("Enter numbers for third row")
for i in range(3):
    data = int(input())
    list3.append(data)

matrix = [list1, list2, list3]
matrix_error = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
if matrix == matrix_error:
    print("This matrix is not possible")
else:
    print()
    printmatrix()
    print()
    # for first pivot element
    print("For first pivot element enter the values")
    pivotelement()
    printmatrix()
    print()

    # for second pivot element
    print("For second pivot element enter the values")
    print()
    pivotelement()
    printmatrix()
    print()

    # for third pivot element
    print("For third pivot element enter the values")
    print()
    pivotelement()
    # changing -0 to 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == -0:
                matrix[i][j] = 0
            else:
                continue
    printmatrix()
    print()
