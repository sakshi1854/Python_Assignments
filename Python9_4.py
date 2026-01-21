# Write a program which accepts one number and prints cube of that number.

def Cube(No1):
    return No1*No1*No1


def main():
    No1=int(input("Enter the number:"))
    Result=0
    Result=Cube(No1)
    print(Result)

if __name__=="__main__":
    main()