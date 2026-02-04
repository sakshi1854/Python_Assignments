# Search a word in file.
# Problem statement-Write a program which accepts the file name and a word from the user and checks whether the word is present in the file ornot.
# Input:Demo.txt Marvellous
#Expected Output:Display whether the word Marvellous is found in the Demo.txt or not.

def FindWord(FileName,Word):
    Ret=False
    fobj=open(FileName,"r")
    for line in fobj:
        words=line.split()
        for w in words:
            if w==Word:
                Ret=True
    fobj.close()
    return Ret

def main():
    FileName=input("Enter the name of the file:")
    Word=input("Enter the word to search:")
    Ret=FindWord(FileName,Word)
    if(Ret==True):
        print("The word is present in the file.")
    else:
        print("The word is not present in the file.")

if __name__=="__main__":
    main()