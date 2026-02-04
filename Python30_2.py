#Count words in a file.
#Problem Statement-Write a program which accepts a filename from the user and count the total number of words in that file.
#Input:Demo.txt 
#Expected Result:Total number of words in Demo.txt

def CountWords(FileName):
    fobj=open(FileName,"r")
    Count=0
    for line in fobj:
        words=line.split()
        for w in words:
            Count=Count+1
    
    fobj.close()
    return Count

def main():
    FileName=input("Enter the name of the file:")
    Ret=CountWords(FileName)
    print(f"The Total number of words in the {FileName} are:{Ret}")


if __name__=="__main__":
    main()