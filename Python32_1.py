# Please follow below rules while designing automation script as :
# Accept input through command line or through files.
# Display any message in log file instead of console.
# For separate task define separate function.
# For robustness handle every expected exception.
# Perform validations before taking any actions.
#Create user defined modules to store the functionality.

#1] Design automation script which accept directory name and calculate the checksum of all files .
# Usage: DirectoryCheckSum.py "Demo"
# Demo is the name of directory.

import os
import hashlib
import sys

def CheckSumCalculate(DirName):
    Ret=False
    Ret=os.path.exists(DirName)
    if(Ret==False):
        print("There is no such directory.")
        return 
    Ret=os.path.isdir(DirName)
    if(Ret==False):
        print("It is not valid directory.")
        return 
    
    fobj=open("MarvellousLogFile.log","w")
    fobj.write("CheckSums of the files in directory are as follows:"+"\n")

    for FolderName,SubFolderName,FileName in os.walk(DirName):
        for fname in FileName:
            fname=os.path.join(FolderName,fname)
            Result=CalculateCheckSum(fname)
            fobj.write(f"The checksum of {fname} is {Result}\n")
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
    if(len(sys.argv)!=2):
        print("Invalid number of command line arguments.")
        return 
    
    CheckSumCalculate(sys.argv[1])


if __name__=="__main__":
    main()