# Write a program which accept one number from user and return addition of its factor.
# Input:12           Output:16  (1+2+3+4+6)

def AdditionFactor(No1):
    Sum=0
    for i in range(1,No1):
        if No1%i==0:
            Sum=Sum+i
    print(Sum)
    
def main():
    No1=int(input("Enter the number:"))
    AdditionFactor(No1)

if __name__=="__main__":
    main()