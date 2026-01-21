# Write a program which accepts two numbers and print addition,subtraction,multiplication and division.

def Addition(No1,No2):
    print(No1+No2)

def Substraction(No1,No2):
    print(No1-No2)

def Multiplication(No1,No2):
    print(No1*No2)

def Division(No1,No2):
    print(No1/No2)

def main():
    No1=int(input("Enter the first number:"))
    No2=int(input("Enter the second number:"))
    Addition(No1,No2)
    Substraction(No1,No2)
    Multiplication(No1,No2)
    Division(No1,No2)

if __name__=="__main__":
    main()