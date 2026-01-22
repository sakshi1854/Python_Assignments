# Write a lambda function which accepts two numbers and returns minimum number.

Minimum=lambda No1,No2:No1 if No1<No2 else No2

def main():
    No1=int(input("Enter the first number:"))
    No2=int(input("Enter the second number:"))
    Ret=Minimum(No1,No2)
    print(Ret)

if __name__=="__main__":
    main()