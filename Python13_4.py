# Write a program which accepts one number and prints binary equivalent.

def PrintBinary(No1):
    result=""
    while No1>0:
        r=No1%2
        result=str(r)+result
        No1=No1//2
    print(int(result))

def main():
    No1=int(input("Enter the number:"))
    PrintBinary(No1)

if __name__=="__main__":
    main()