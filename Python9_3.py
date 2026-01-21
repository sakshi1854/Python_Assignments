# Write a program which accepts one number and prints square of that number
# Input:5
# Output: 25


def Square(No1):
    return No1*No1

def main():
    No1=int(input("Enter the number:"))
    Result=0
    Result=Square(No1)
    print(Result)

if __name__=="__main__":
    main()