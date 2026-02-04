# Check file exists in current directory.
# Problem statement- write a program which accepts a filename from the user and checks whether file exists in the current directory or not.
# Input - Demo.txt
# Expected output - Display whether Demo.txt exists or not.

import os

def CheckExistence(FileName):
    Ret=False
    Ret=os.path.exists(FileName)
    if Ret==True:
        print(f"{FileName} exists in the current directory.")
    else:
        print(f"{FileName} does not exists in the current directory.")

def main():
    FileName=input("Enter the name of the file:")
    CheckExistence(FileName)


if __name__=="__main__":
    main()