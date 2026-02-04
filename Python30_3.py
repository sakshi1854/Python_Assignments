# Display file line by line.
# Problem statement- Write a program which accepts a filename from user and displays the content of the file line by line on the screem.
# Input:Demo.txt
# Expected output:Display each line of Demo.txt one by one.

def FileContent(FileName):
    fobj=open(FileName,"r")
    for line in fobj:
        print(line)
    fobj.close()

def main():
    FileName=input("Enter the name of the file:")
    FileContent(FileName)


if __name__=="__main__":
    main()