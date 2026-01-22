# Write a lambda function which accepts one number and returns cube of that number.

Cube=lambda No:No*No*No

def main():
    No1=int(input("Enter the number:"))
    Ret=Cube(No1)
    print(Ret)

if __name__=="__main__":
    main()