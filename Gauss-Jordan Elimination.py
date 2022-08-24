# python program for gauss-jordan method in a 3*3 matrix
# function to print list in a matrix form
def printmatrix():
    for i in matrix:
        for j in i:
            # if you want more or less numbers after decimal point to adjust %.nf accordingly where n is the number
            # of units
            print("%.1f" % j, end="  ")
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
    print("%.1f" % pivot_element, "is pivot element")
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


# to solve the pivot column and remove negative sign from all zeros.
def solve_pivotelement():
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


# this function will be used to solve the number of time we'll have to solve pivot column
def no_of_pivot_element():
    print()
    printmatrix()
    print()
    for i in range(row_number):
        number = ["first", "second", "third", "fourth", "fifth", "sixth"]
        n = i
        print("For", number[n], "pivot element enter the values of row and column")
        solve_pivotelement()

# taking input for rows and column
print("What type of matrix do you want to solve")
row_number = int(input("rows : "))
print(row_number)
column_number = int(input("columns : "))
print(column_number)
# setting some pre-conditions
if column_number != row_number:
    print("Sorry! cannot solve this matrix the number of rows and column must be equal. This program only supports "
          "matrices (2*2 to 6*6).")
    quit()
elif column_number > 6 and row_number > 6:
    print("Sorry! cannot solve this matrix the number of rows and column must be equal. This program only supports "
          "matrices (2*2 to 6*6).")
    quit()
elif column_number <= 1 and row_number <= 1:
    print("This matrix is not possible")
    quit()

n = 0
# taking input for matrix
matrix = [[0 for i in range(column_number)] for x in range(row_number)]
while n != row_number:
    number = ["first", "second", "third", "fourth", "fifth", "sixth"]
    print()
    print("Enter numbers for", number[n], "row")
    for i in range(column_number):
        data = int(input())
        matrix[n][i] = data
    n = n + 1
# This matrix is not solvable i.e gives an error
matrix_error = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
if matrix == matrix_error:
    print("This matrix is not possible")

elif column_number == 2 and row_number == 2:
    no_of_pivot_element()
    print()
    print("This is the final matrix.")

elif column_number == 3 and row_number == 3:
    no_of_pivot_element()
    print()
    print("This is the final matrix.")

elif column_number == 4 and row_number == 4:
    no_of_pivot_element()
    print()
    print("This is the final matrix.")

elif column_number == 5 and row_number == 5:
    no_of_pivot_element()
    print()
    print("This is the final matrix.")

elif column_number == 6 and row_number == 6:
    no_of_pivot_element()
    print()
    print("This is the final matrix.")
