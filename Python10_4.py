# Write a program which accepts one number and prints all the even numbers till that number.
# Input: 10
# Output: 2 4 6 8 10

def CheckEven(No1):
    Ret=list()
    for i in range(1,No1+1):
        if i%2==0:
            Ret.append(i)
    return Ret

def main():
    No1=int(input("Enter the number:"))
    Result=list()
    Result=CheckEven(No1)
    print(Result)

if __name__=="__main__":
    main()