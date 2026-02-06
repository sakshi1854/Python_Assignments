# Design an automation script which accept directory name and write name of duplicate files from that directory into log file.
# named as Log.txt. Log.txt file should be created into current directory.
# Usage: DirectoryDuplicate.py "Demo"
# Demo is the name of directory.

import sys
import os
import hashlib


def FindDuplicates(DirName):
    Ret=False
    Ret=os.path.exists(DirName)
    if(Ret==False):
        print("There is no such directory.")
        return
    Ret=os.path.isdir(DirName)
    if(Ret==False):
        print("It is not a correct directory name.")
        return 
    
    fobj=open("Log.txt","w")
    fobj.write("These is the log file which contains the duplicate file names.\n")

    Dict={}

    for FolderName,SubFolderName,FileName in os.walk(DirName):
        for fname in FileName:
            fname=os.path.join(FolderName,fname)
            CheckSum=CalculateCheckSum(fname)

            if CheckSum in Dict:
                Dict[CheckSum].append(fname)
            else:
                Dict[CheckSum]=[fname]

    for files in Dict.values():
        if(len(files)>1):
            for f in files:
                fobj.write(f+"\n")
        
    fobj.close()

def CalculateCheckSum(FileName):
    fobj=open(FileName,"rb")
    hobj=hashlib.md5()
    Buffer=fobj.read(1000)
    while(len(Buffer)>0):
        hobj.update(Buffer)
        Buffer=fobj.read(1000)
    fobj.close()
    return hobj.hexdigest()

def main():
    if(len(sys.argv)<2):
        print("Invalid number of command line arguments.")
        return
    
    FindDuplicates(sys.argv[1])


if __name__=="__main__":
    main()