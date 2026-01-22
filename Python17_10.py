# Write a python Program which accept number from user and return addition of digits in that number.
# Input: 5187934          Output: 37

def Addition(No1):
    Sum=0
    while No1!=0:
        Digit=No1%10
        Sum=Sum+Digit
        No1=No1//10
    return Sum

def main():
    No1=int(input("Enter the number:"))
    Ret=Addition(No1)
    print(Ret)

if __name__=="__main__":
    main()