# Write a program which contains filter(),map(),reduce() in it.Python application which contains one list of numbers.List contains the numbers which are accepted from user.Filter should filter out all such numbers which are even.Map function will calculate its square.Reduce will return addition of all that numbers.
# Input List=[5,2,3,4,3,4,1,2,8,10]
# List after filter=[2,4,4,2,8,10]
# List after map=[4,16,16,4,64,100]
# Output of reduce=204

from functools import reduce

CheckEven=lambda No1:No1%2==0

Square=lambda No1:No1*No1

Addition=lambda No1,No2:No1+No2

def main():
    No1=int(input("Enter the number:"))
    Data=list()
    for i in range(No1):
        Ret=int(input())
        Data.append(Ret)
    print("The Original Data is:",Data)
    FData=list(filter(CheckEven,Data))
    print("The Data after filter is:",FData)
    MData=list(map(Square,FData))
    print("The Data after map is:",MData)
    RData=reduce(Addition,MData)
    print("The Data after Reduce is:",RData)

if __name__=="__main__":
    main()