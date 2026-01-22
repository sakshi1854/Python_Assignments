# Write a program which accept number from user and return number of digits in that number.
# Input : 5187934        Output:7

def CountDigits(No1):
    Count=0
    while No1!=0:
        Digit=No1%10
        Count=Count+1
        No1=No1//10
    print(Count)
    
def main():
    No1=int(input("Enter the number:"))
    CountDigits(No1)

if __name__=="__main__":
    main()