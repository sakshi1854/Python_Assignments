# Write a lambda function which accepts one number and returns True if divisible by 5.

CheckDivisible=lambda No1:No1%5==0

def main():
    No1=int(input("Enter the number:"))
    Ret=CheckDivisible(No1)
    print(Ret)

if __name__=="__main__":
    main()