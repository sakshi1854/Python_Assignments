# Write a lambda function using reduce() which accepts a list of numbers and returns the maximum element.
from functools import reduce

CheckMax=lambda A,B:A if A>=B else B

def main():
    Data=[1,2,3,4,5]
    print(Data)
    RData=reduce(CheckMax,Data)
    print(RData)

if __name__=="__main__":
    main()