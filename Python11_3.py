# Write a program which accepts one number and prints sum of digits
#Input:123
# Output:6

def SumDigits(No1):
    Num=No1
    Sum=0
    while Num!=0:
        Sum=Sum+(Num%10)
        Num=Num//10
    return Sum

def main():
    No1=int(input("Enter the number:"))
    Result=0
    Result=SumDigits(No1)
    print(Result)

if __name__=="__main__":
    main()