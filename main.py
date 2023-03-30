matrix = [[2,5,4], [5,2.453432,7], [5,8,9]]
def printmatrix():
    print("---------------------------")
    for i in matrix:
        for j in i:
            if j == -0: # this condition is used to change -0 to 0s
                j = 0
            elif j % 1 == 0:
                j = "%.0f" % j
            elif j % 1 != 0:
                j = "%.2f" % j
            # if you want more or less numbers after decimal point to adjust %.nf accordingly where n is the number
            # of units after decimal points
            print(j, end="  ")
        print()
    print("---------------------------")

printmatrix()





