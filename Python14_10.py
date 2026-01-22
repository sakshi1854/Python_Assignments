# Write a lambda function which accepts three numbers and returns the largest number.

Largest=lambda No1,No2,No3:No1 if(No1>=No2 and No1>=No3) else (No2 if No2>=No3 else No3)

def main():
    No1=int(input("Enter the first number:"))
    No2=int(input("Enter the second number:"))
    No3=int(input("Enter the third number:"))

    Ret=Largest(No1,No2,No3)
    print(Ret)

if __name__=="__main__":
    main()