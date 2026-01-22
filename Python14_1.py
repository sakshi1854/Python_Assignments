# Write a lambda function which accepts one number and returns square of that number.

Square=lambda No:No*No

def main():
    No1=int(input("Enter the number:"))
    Ret=Square(No1)
    print(Ret)

if __name__=="__main__":
    main()