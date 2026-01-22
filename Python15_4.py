# Write a lambda function using reduce() which accepts a list of numbers and returns the addition of all elements.
from functools import reduce

Addition=lambda A,B:A+B

def main():
    Data=[1,2,3,4,5]
    print(Data)
    RData=reduce(Addition,Data)
    print(RData)

if __name__=="__main__":
    main()