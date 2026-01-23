# Write a program which contains filter(),map(), and reduce() in it.Python application which contains one list of numbers.List contains the numbers which are accepted from user.Filter should filter out all such elements which are greater than or equal to 70 and less than or equal to 90.Map function will increase each number by 10.Reduce will return product of numbers.
# Input List=[4,34,36,76,68,24,89,23,86,90,45,70]
# List after filter=[76,89,86,90,70]
# List after map=[86,99,96,100,80]
# Output of the reduce =6538752000

from functools import reduce

CheckRange=lambda No1:No1>=70 and No1<=90

Increment=lambda No1:No1+10

Multiplication=lambda No1,No2:No1*No2

def main():
    No1=int(input("Enter the number of elements:"))
    Data=list()
    print("Enter the elements:")
    for i in range(No1):
        Ret=int(input())
        Data.append(Ret)
    print("The original Data is:",Data)
    FData=list(filter(CheckRange,Data))
    print("The Data after filter is:",FData)
    MData=list(map(Increment,FData))
    print("The Data after map is:",MData)
    RData=reduce(Multiplication,MData)
    print("The Data after reduce is:",RData)

if __name__=="__main__":
    main()