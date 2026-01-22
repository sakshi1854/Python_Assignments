# Write a program which accept one number from user and return its factorial.
# Input: 5                      Output:120


def PrintFactorial(No1):
    Fact=1
    for i in range(1,No1+1):
        Fact=Fact*i
    print(Fact)

def main():
    No1=int(input("Enter the number:"))
    PrintFactorial(No1)

if __name__=="__main__":
    main()