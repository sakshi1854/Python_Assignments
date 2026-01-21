# Write a program which contains one function ChkGreater() that accepts two numbers and prints the greater number.

def ChkGreater(No1,No2):
    if No1>No2:
        print(No1,"is greater number")
    else:
        print(No2,"is greater number")

def main():
    No1=int(input("Enter first number:"))
    No2=int(input("Enter second number:"))
    ChkGreater(No1,No2)


if __name__=="__main__":
    main()