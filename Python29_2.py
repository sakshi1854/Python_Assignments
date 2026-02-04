# Display the file contents.
# Problem statement- Write a program which accepts a file name from the user,opens that file,and display the entire contents on that console.
# Input-Demo.txt
# Expected Output-Display contents of Demo.txt on console.

import os

def ReadContent(FileName):
    Ret=False
    Ret=os.path.exists(FileName)
    if(Ret==True):
        fobj=open(FileName,"r")
        Data=fobj.read()
        print(Data)
        fobj.close()
    else:
        print("File Does not exists")


def main():
    FileName=input("Enter the name of the file:")
    ReadContent(FileName)


if __name__=="__main__":
    main()

