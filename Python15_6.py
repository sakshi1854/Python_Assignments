#Write a lambda function using reduce() which accepts a list of numbers and returns the minimum elements.
from functools import reduce

CheckMin=lambda No1,No2:No1 if No1<=No2 else No2

def main():
    Data=[1,2,3,4,5,6]
    print(Data)
    RData=reduce(CheckMin,Data)
    print(RData)

if __name__=="__main__":
    main()