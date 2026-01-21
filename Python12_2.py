# Write a program which accepts one number and print its factor.
# Input : 12
# Output: 1 2 3 4 6 12

def PrintFactor(No1):
    Ret=list()
    for i in range(1,No1+1):
        if No1%i==0:
            Ret.append(i)
    return Ret

def main():
    No1=int(input("Enter the number:"))
    Result=list()
    Result=PrintFactor(No1)
    print(Result)

if __name__=="__main__":
    main()