# Design an automation script which accept directory name and delete all duplicate files from that directory.write names of duplicate files from that directory.
#Write names of duplicate files from that directory into log file named as Log.txt.
# Log.txt file should be created into current directory.Display execution time required for the script.
#Usage:DirectoryDuplicateRemoval.py  "Demo"
#Demo is the name of directory.

import sys
import os
import hashlib
import time

def DeleteDuplicate(DirectoryName):
    Ret=False
    Ret=os.path.exists(DirectoryName)
    if(Ret==False):
        print("There is no such directory.")
        return 
    Ret=os.path.isdir(DirectoryName)
    if(Ret==False):
        print("It is not a valid directory.")
        return 
    Dictionary={}
    for FolderName,SubFolderName,FileName in os.walk(DirectoryName):
        for fname in FileName:
            fname=os.path.join(FolderName,fname)
            CheckSum=CalculateCheckSum(fname)
            if CheckSum in Dictionary:
                Dictionary[CheckSum].append(fname)
            else:
                Dictionary[CheckSum]=[fname]
    return Dictionary

def CalculateCheckSum(FileName):
    fobj=open(FileName,"rb")
    hobj=hashlib.md5()
    Buffer=fobj.read(1000)
    while(len(Buffer)>0):
        hobj.update(Buffer)
        Buffer=fobj.read(1000)
    fobj.close()
    return hobj.hexdigest()

def DeleteDuplicateFiles(DirectoryName):
    MyDict=DeleteDuplicate(DirectoryName)
    Result=list(filter(lambda x:len(x)>1,MyDict.values()))
    fobj=open("Marvellous.log","w")
    fobj.write("This file contains the duplicated and deleted file record.")

    Count=0
    for value in Result:
        for subvalue in value:
            Count=Count+1
            if(Count>1):
                fobj.write(f"{subvalue}\n")
                os.remove(subvalue)
        Count=0
    fobj.close()

def main():
    if(len(sys.argv)!=2):
        print("Invalid number of arguments.")
        return 
    fobj=open("Marvellous.log","w")
    start_time=time.time()
    DeleteDuplicateFiles(sys.argv[1])
    end_time=time.time()
    fobj.write(f"The total execution time required for the execution is:{end_time-start_time}\n")
    fobj.close()

if __name__=="__main__":
    main()