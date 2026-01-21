# Write a program which accepts one number and prints multiplication table of that number.
# Input:4
# Output: 4 8 12 16 20 24 28 32 36 40

def MultiplicationTable(No1):
    Ret=list()
    for i in range(1,11):
        Ret.append(No1*i)
    return Ret

def main():
    No1=int(input("Enter the number:"))
    Result=list()
    Result=MultiplicationTable(No1)
    print(Result)


if __name__=="__main__":
    main()