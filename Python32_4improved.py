import sys
import os
import hashlib
import time

def DeleteDuplicate(DirectoryName):
    Ret=os.path.exists(DirectoryName)
    if(Ret==False):
        print("There is no such directory.")
        return None
    Ret=os.path.isdir(DirectoryName)
    if(Ret==False):
        print("It is not a valid directory.")
        return None
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

def DeleteDuplicateFiles(DirectoryName,fobj):
    MyDict=DeleteDuplicate(DirectoryName)
    if MyDict is None:
        return 
    Result=list(filter(lambda x:len(x)>1,MyDict.values()))

    Count=0
    for value in Result:
        for subvalue in value:
            Count=Count+1
            if(Count>1):
                fobj.write(subvalue+"\n")
                try:
                    os.remove(subvalue)
                except:
                    pass
        Count=0

def main():
    if(len(sys.argv)!=2):
        print("Invalid number of arguments.")
        return
    
    fobj=open("Marvellous.log","w")
    fobj.write("This file contains the duplicated and deleted file record.\n")

    start_time=time.time()
    DeleteDuplicateFiles(sys.argv[1],fobj)
    end_time=time.time()

    fobj.write(f"The total execution time required for execution is:{end_time-start_time}\n")
    fobj.close()

if __name__=="__main__":
    main()