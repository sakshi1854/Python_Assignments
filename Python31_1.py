#Please follow below rules while designing automation script as
# Accept the input through command line or through file.
# Display any message in log file instead of console.
# For separate task define separate function.
# For robustness handle every expected exception.
# Perform validations before taking any action.
# Create user defined modules to store the functionality.
#Design automation script which accpet directory name and file extension from user.Display all files with that extension.
#Usage:DirectoryFileSearch.py "Demo" ".txt"
#Demo is the name of directory and .txt is the extension that we want to search.

import sys
import os

def DirectoryScanner(DirectoryName,Extension):
    Ret=False
    Ret=os.path.exists(DirectoryName)
    if(Ret==False):
        print("There is no such directory.")
        return 
    Ret=os.path.isdir(DirectoryName)
    if(Ret==False):
        print("It is not a valid directory name.")
        return 
    
    for FolderName,SubFolderName,FileName in os.walk(DirectoryName):
        for fname in FileName:
            if(fname.endswith(Extension)):
                print(fname,end=" ")
        print()

def main():
    if(len(sys.argv)<3):
        print("Invalid number of command line arguments.")
        return 
    DirectoryName=sys.argv[1]
    Extension=sys.argv[2]
    DirectoryScanner(DirectoryName,Extension)

if __name__=="__main__":
    main()