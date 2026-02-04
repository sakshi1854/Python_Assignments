#Copy file contents into another file.
#Problem Statement- write a program which accepts two file names from the user.
# First file is an existing file.
# Second file is a new file.
# Copy all the contents from the first file into second file.
#Input : ABC.txt Demo.txt
#Expected Output: Contents of ABC.txt copied into Demo.txt

def CopyContent(FileName1,FileName2):
    fobj=open(FileName1,"r")
    foobj=open(FileName2,"w")

    Buffer=fobj.read(1024)
    while(len(Buffer)>0):
        foobj.write(Buffer)
        Buffer=fobj.read(1024)
    print("The file gets copied successfully.")
    fobj.close()
    foobj.close()

def main():
    FileName1=input("Enter the name of the file:")
    FileName2=input("Enter the name of the file to create:")
    CopyContent(FileName1,FileName2)


if __name__=="__main__":
    main()