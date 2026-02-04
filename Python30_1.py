# Count Lines in a file.
# Problem Statement- Write a program which accepts a file name from the user and count how many lines are present in the file.
# Input:Demo.txt
# Expected output:Total number of lines in Demo.txt


def CountLines(FileName):
    Count=0
    fobj=open(FileName,"r")
    for line in fobj:
        Count=Count+1
    fobj.close()
    return Count

def main():
    FileName=input("Enter the name of the file:")
    Ret=CountLines(FileName)
    print(f"Total number of lines in {FileName} is:{Ret}")


if __name__=="__main__":
    main()