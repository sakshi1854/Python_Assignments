#Write a lambda function using reduce() which accepts a list of numbers and returns the product of all the elements.

from functools import reduce

Product=lambda No1,No2:No1*No2

def main():
    Data=[10,20,30,40,50,60]
    print(Data)
    RData=reduce(Product,Data)
    print(RData)

if __name__=="__main__":
    main()