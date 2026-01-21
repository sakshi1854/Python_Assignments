# Write a program which accepts one number and prints sum of first N natural numbers.
# Input : 5
# Output : 15

def Sum(No1):
    Ret=0
    for i in range(1,No1+1):
        Ret=Ret+i
    return Ret

def main():
    No1=int(input("Enter the number:"))
    Result=Sum(No1)
    print(Result)

if __name__=="__main__":
    main()