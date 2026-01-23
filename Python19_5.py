# Write a program which contains filter(),map(),and reduce() in it.Python application which contains one list of numbers.List contains the numbers which are accepted from user.Filter should filter out all prime numbers.Map function will multiply each number by 2.Reduce will return maximum number from that number.(You can also use normal functions instead of lambda function).
# Input List=[2,70,11,10,17,23,31,77]
# List after Filter=[2,11,17,23,31]
# List after map=[4,22,34,46,62]
# Output of reduce = 62

from functools import reduce

def CheckPrime(No1):
    if No1<=1:
        return False
    for i in range(2,No1//2+1):
        if No1%i==0:
            return False
    return True

Multiply=lambda No1:No1*2

Maximum=lambda No1,No2:No1 if No1>No2 else No2

def main():
    No1=int(input("Enter the number:"))
    Data=list()
    print("Enter the elements:")
    for i in range(No1):
        Ret=int(input())
        Data.append(Ret)
    print("The Original Data is:",Data)
    FData=list(filter(CheckPrime,Data))
    print("The Data after filter is:",FData)
    MData=list(map(Multiply,FData))
    print("The Data after map is:",MData)
    RData=reduce(Maximum,MData)
    print("The Data after reduce is:",RData)

if __name__=="__main__":
    main()