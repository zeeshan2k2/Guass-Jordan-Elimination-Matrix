print("What type of matrix do you want to solve")
row_number = int(input("rows : "))
print(row_number)
column_number = int(input("columns : "))
print(column_number)

n = 0
matrix = [[0 for i in range(column_number)] for x in range(row_number)]
while n != row_number:
    number = ["first", "second", "third", "fourth", "fifth", "sixth"]
    print()
    print("Enter numbers for", number[n], "row")
    for i in range(column_number):
        data = int(input())
        matrix[n][i] = data
    n = n + 1

def printmatrix():
    print("---------------------------")
    for i in matrix:
        for j in i:
            if j == -0: # this condition is used to change -0 to 0.
                j = 0
            #if the number is whole number in matrix it prints it without printing any zeros
            # after decimal point
            elif j % 1 == 0:
                j = "%.0f" % j
            # if the number is not whole number in matrix it prints two number after decimal point
            # i.e for 2.346446 = 2.34 you can change it by increasing or decreasing number of n in
            #"%.nf" % j where n will be the numbers after decimal point
            elif j % 1 != 0:
                j = "%.2f" % j
            print(j, end="  ")
        print()
    print("---------------------------")

printmatrix()