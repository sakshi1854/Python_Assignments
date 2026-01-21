#Write a program which accepts one number and prints factorial of that number.
# Input:5
# Output: 120

def Factorial(No1):
    Ret=1
    for i in range(1,No1+1):
        Ret=Ret*i
    return Ret

def main():
    No1=int(input("Enter the number:"))
    Result=0
    Result=Factorial(No1)
    print(Result)

if __name__=="__main__":
    main()