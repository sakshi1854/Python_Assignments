# Write a program which accept one number and display below pattern.
# Input: 5
# Output: 1 2 3 4 5
#         1 2 3 4 5
#         1 2 3 4 5
#         1 2 3 4 5
#         1 2 3 4 5

def PrintPattern(No1):
    for i in range(No1):
        for j in range(No1):
            print(j+1,end=" ")
        print()

PrintPattern(5)