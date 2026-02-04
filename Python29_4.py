# Compare two files (Command Line)
#Problem Statement: Write a program which accepts two names through command line arguments and compares the contents of both the files.
#If both files contains the same contents,display success.
# Otherwise display failure.
# Input :Command Line: Demo.txt ABC.txt
#Expected output:Success or failure.

import sys

def CheckSimilarity(FileName1,FileName2):
    fobj=open(FileName1,"r")
    foobj=open(FileName2,"r")

    while True:
        Buffer1=fobj.read(1024)
        Buffer2=foobj.read(1024)

        if Buffer1!=Buffer2:
            print("Failure")
            break
        
        if Buffer1=="" and Buffer2=="":
            print("Success")
            break
    fobj.close()
    foobj.close()

def main():
    if(len(sys.argv)<3):
        print("Insufficient command line arguments.")
        return
    FileName1=sys.argv[1]
    FileName2=sys.argv[2]
    CheckSimilarity(FileName1,FileName2)


if __name__=="__main__":
    main()