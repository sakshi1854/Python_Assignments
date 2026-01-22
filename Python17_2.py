# Write a program which accepts one number and display below pattern.
# Input : 5
# Output:   * * * * *
#            * * * * *
#            * * * * *
#            * * * * *
#            * * * * *


def PrintPattern(No1):
    for i in range(No1):
        for j in range(No1):
            print("*",end=" ")
        print()

PrintPattern(5)