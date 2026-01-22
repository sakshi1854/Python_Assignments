# Write a program which accept one number for user and check whether number is prime or not.
# Input : 5                  Output:It is prime number

def CheckPrime(No1):
    if No1<=1:
        print("It is not prime number")
        return
    isPrime=True
    for i in range(2,No1//2+1):
        if No1%i==0:
            isPrime=False
            break
    if isPrime:
        print("It is prime number")
    else:
        print("It is not prime number")

def main():
    No1=int(input("Enter the number:"))
    CheckPrime(No1)

if __name__=="__main__":
    main()