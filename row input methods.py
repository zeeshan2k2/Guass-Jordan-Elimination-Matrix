# function to print list in a matrix form
def printmatrix():
    for i in matrix:
        for j in i:
            # if you want more or less numbers after decimal point to adjust %.nf accordingly where n is the number
            # of units after decimal points
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
    for i in range(len(matrix[rows])):
        matrix[rows][i] = matrix[rows][i] / pivot_element
    for row in range(len(matrix)):
        if row == rows:
            continue
        else:
            make_zero = matrix[row][colm]
            for col in range(len(matrix[colm])):
                matrix[row][col] = matrix[row][col] - make_zero * matrix[rows][col]








    # for i in range(len(matrix)):
    #     matrix[rows][i] = matrix[rows][i] / pivot_element
    # for row in range(len(matrix)):
    #     if row == rows:
    #         continue
    #     else:
    #         make_zero = matrix[row][colm]
    #         for col in range(len(matrix)):
    #             matrix[row][col] = matrix[row][col] - make_zero * matrix[rows][col]

matrix = [[4, 6, 8], [5, 3, 9], [3, 4, 6], [8, 7, 4]]
printmatrix()
pivotelement()
printmatrix()

























# # to solve the pivot column and remove negative sign from all zeros.
# def solve_pivotelement():
#     print()
#     pivotelement()
#     # changing -0 to 0
#     for i in range(len(matrix)):
#         for j in range(len(matrix)):
#             if matrix[i][j] == -0:
#                 matrix[i][j] = 0
#             else:
#                 continue
#     printmatrix()
#     print()
#
# def no_of_pivot_element():
#     print()
#     printmatrix()
#     print()
#     if row_number > column_number:
#         for i in range(column_number - 1):
#             number = ["first", "second", "third", "fourth", "fifth", "sixth"]
#             n = i
#             print("For", number[n], "pivot element enter the values of row and column")
#             solve_pivotelement()
#         print("This is the final Matrix.")
#
# # taking input for rows and column
# print("What type of matrix do you want to solve")
# row_number = int(input("rows : "))
# print(row_number)
# column_number = int(input("columns : "))
# print(column_number)
#
# n = 0
# # taking input for matrix
# matrix = [[0 for i in range(column_number)] for x in range(row_number)]
# while n != row_number:
#     number = ["first", "second", "third", "fourth", "fifth", "sixth"]
#     print()
#     print("Enter numbers for", number[n], "row")
#     for i in range(column_number):
#         data = int(input())
#         matrix[n][i] = data
#     n = n + 1
#
# # This matrix is not solvable i.e gives an error
# matrix_error = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# if matrix == matrix_error:
#     print("This matrix is not possible")
# else:
#     no_of_pivot_element()