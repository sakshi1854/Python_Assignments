#Frequency of a string in file.
# Problem statement-Write a program which accepts a file name and one string from the user and returns the frequency count of occurenecs of that string in the file.
# Input Demo.txt Marvellous
#Expected output: Count how many times "Marvellous" appears in Demo.txt

import sys

def CountFrequency(FileName,Word):
    fobj=open(FileName,"r")
    count=0
    for line in fobj:
        words=line.split()
        for w in words:
            if w==Word:
                count=count+1
    fobj.close()
    return count

def main():
    if(len(sys.argv)<3):
        print("Insufficient command line arguments")
        return
    
    FileName=sys.argv[1]
    Word=sys.argv[2]

    result=CountFrequency(FileName,Word)
    print("Frequency is:",result)


if __name__=="__main__":
    main()