# Write a function which accepts two numbers and returns addition.

Addition=lambda No1,No2:No1+No2

def main():
    No1=int(input("Enter the first number:"))
    No2=int(input("Enter the second number:"))
    Ret=Addition(No1,No2)
    print(Ret)

if __name__=="__main__":
    main()