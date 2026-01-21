# Write a program which accepts one number and checks whether it is prime or not.
# Input:11
# Output: Prime Number

def CheckPrime(No1):
    if No1<=1:
        print(No1,"is not a prime number")
    else:
        is_Prime=True
        for i in range(2,int(No1**0.5)+1):
            if No1%i==0:
                is_Prime=False
                break
        if is_Prime==True:
            print(No1,"is prime number")
        else:
            print(No1,"is not a prime number")

def main():
    No1=int(input("Enter the number:"))
    CheckPrime(No1)

if __name__=="__main__":
    main()