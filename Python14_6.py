# Write a lambda function which accepts one number and return True if number is Odd otherwise False.

CheckOdd=lambda No1:No1%2!=0

def main():
    No1=int(input("Enter the number:"))
    Ret=CheckOdd(No1)
    print(Ret)

if __name__=="__main__":
    main()