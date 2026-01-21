# Write a program which accepts one number and prints all odd numbers till that number.

def CheckOdd(No1):
    Ret=list()
    for i in range(1,No1+1):
        if i%2!=0:
            Ret.append(i)
    return Ret

def main():
    No1=int(input("Enter the number:"))
    Result=list()
    Result=CheckOdd(No1)
    print(Result)

if __name__=="__main__":
    main()