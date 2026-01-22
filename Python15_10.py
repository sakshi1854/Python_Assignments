#Write a lambda function using filter() which accepts a list of numbers and returns count of even numbers.

CheckEven=lambda No:No%2==0

def main():
    Data=[1,2,3,4,5,6,7,8,9,10]
    print(Data)
    FData=len(list(filter(CheckEven,Data)))
    print(FData)

if __name__=="__main__":
    main()