# Write a program which accepts one number and prints count of digits in that number.
# Input:7521
# Output: 4

def CountDigits(No1):
    Count=0
    Num=No1
    while Num!=0:
        Count=Count+1
        Num=Num//10
    return Count

def main():
    No1=int(input("Enter the number:"))
    Result=0
    Result=CountDigits(No1)
    print(Result)

if __name__=="__main__":
    main()