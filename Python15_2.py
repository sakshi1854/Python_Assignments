# Write a lambda function using filter() which accepts a list on numbers and returns a list of even numbers.

CheckEven=lambda No:No%2==0

def main():
    Data=[1,2,3,4,5,6,7,8,9,10]
    print(Data)
    FData=list(filter(CheckEven,Data))
    print(FData)

if __name__=="__main__":
    main()