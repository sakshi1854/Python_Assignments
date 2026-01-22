# Create on module named as Arithmetic which contains 4 functions as Add() for addition,Sub() for substraction,Mult() for multiplication,Div() for division.All functions accepts two parameters as number and perform the operation.write on python program which call all the functions from Arithmetic module by accepting the parameters from user.

import Arithmetic

def main():
    No1=int(input("Enter the first number:"))
    No2=int(input("Enter the second number:"))

    Add=Arithmetic.Addition(No1,No2)
    Sub=Arithmetic.Substraction(No1,No2)
    Mult=Arithmetic.Multiplication(No1,No2)
    Div=Arithmetic.Division(No1,No2)

    print(Add)
    print(Sub)
    print(Mult)
    print(Div)

if __name__=="__main__":
    main()
