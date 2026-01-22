# Write a function which accepts one number and returns True if number is even otherwise false.

CheckEven=lambda No1:No1%2==0

def main():
    No1=int(input("Enter the number:"))
    Ret=CheckEven(No1)
    print(Ret)

if __name__=="__main__":
    main()