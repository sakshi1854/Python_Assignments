# Write a program which accepts one number and checks whether it is divisible by 3 and 5.
#Input : 15
#Output : Divisible by 3 and 5

def CheckDivisibility(No1):
    if No1%3==0 and No1%5==0:
        print(No1,"is Divisible by 3 and 5")
    else:
        print(No1,"is not Divisible by 3 and 5")

def main():
    No1=int(input("Enter the number:"))
    CheckDivisibility(No1)

if __name__=="__main__":
    main()