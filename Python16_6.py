# Write a program which accepts number from user and check whether that number is positive or negative or zero.
# Input : 11             Output:Positive number
# Input : -8             Output:Negative number
# Input: 0               Output:Zero

def CheckNumber(No1):
    if No1>0:
        print("Positive Number")
    elif No1<0:
        print("Negative Number")
    else:
        print("Zero")

def main():
    No1=int(input("Enter the number:"))
    CheckNumber(No1)

if __name__=="__main__":
    main()