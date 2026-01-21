# Write a program which accepts one number and prints that many numbers starting from 1.
# Input:5
# Output : 1 2 3 4 5

def PrintRange(No1):
    for i in range(1,No1+1):
        print(i,end=" ")

def main():
    No1=int(input("Enter the number:"))
    PrintRange(No1)

if __name__=="__main__":
    main()