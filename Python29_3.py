# Copy file contents into new file(Command Line.)
# Problem Statement- Write a program which accepts an existing file name through command line arguments.creates a new file named Demo.txt and copies all contents from the given file into Demo.txt.
#Input (Command Line):ABC.txt
#Expected output:Creates a Demo.txt and copy the contents of ABC.txt into Demo.txt


import sys

def CopyContent(FileName):
    fobj=open("ABC.txt","w")
    foobj=open(FileName,"r")
    Buffer=foobj.read(1000)
    while(len(Buffer)>0):
        fobj.write(Buffer)
        Buffer=foobj.read(1000)
    print("File contents gets successfully copied")
    fobj.close()
    foobj.close()


def main():
    if(len(sys.argv)<2):
        print("Please provide the proper input")
        return 
    FileName=sys.argv[1]
    CopyContent(FileName)


if __name__=="__main__":
    main()