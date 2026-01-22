# Write a program which contains one number from user and returns true if number is divisible by 5 otherwise returns false.
# Input:8           Output:False
# Input:25          Output : True

def DivisibilityCheck(No1):
    if No1%5==0:
        return True
    else:
        return False

def main():
    No1=int(input("Enter the number:"))
    print(DivisibilityCheck(No1))


if __name__=="__main__":
    main()



