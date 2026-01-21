# Write a program which accepts one number and prints that many numbers in reverse order.
# Input : 5
# Output : 5 4 3 2 1

def PrintReverse(No1):
    for i in range(No1,0,-1):
        print(i,end=" ")

def main():
    No1=int(input("Enter the number:"))
    PrintReverse(No1)

if __name__=="__main__":
    main()