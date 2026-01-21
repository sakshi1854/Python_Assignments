# Write a program which accepts one number and print reverse of that number.
# Input:123
# Output:321

def PrintReverse(No1):
    Rev=0
    Num=No1
    while Num!=0:
        Digit=Num%10
        Rev=(Rev*10)+Digit
        Num=Num//10
    return Rev

def main():
    No1=int(input("Enter the number:"))
    Result=0
    Result=PrintReverse(No1)
    print(Result)

if __name__=="__main__":
    main()