# Write a program which accept N numbers from user and store it into List.Return addition of all prime numbers from that List.Main python file accepts N numbers from user and pass each number to ChkPrime() function which is a part of our user defined module named as MarvellousNum.Name of the function from main python file should be ListPrime().
# Input : Number of elements:11
# Input Elements: 13 5 45 7 4 56 10 34 2 5 8
# Output: 32 (13+5+7+2+5)

import MarvellousNum

def ListPrime(Data):
    Size=len(Data)
    Sum=0
    for i in range(Size):
        Ret=MarvellousNum.ChkPrime(Data[i])
        if(Ret==True):
            Sum=Sum+Data[i]
    return Sum

if __name__=="__main__":
    No1=int(input("Enter the number of elements:"))
    Data=list()
    print("Enter the elements:")
    for i in range(No1):
        Ret=int(input())
        Data.append(Ret)
    Sum=ListPrime(Data)
    print("The sum of the prime elements from the list is:",Sum)