# Write a lambda function which accepts two numbers and returns maximum number.

Maximum=lambda No1,No2:max(No1,No2)

def main():
    No1=int(input("Enter the first number:"))
    No2=int(input("Enter the second number:"))
    Ret=Maximum(No1,No2)
    print(Ret)

if __name__=="__main__":
    main()