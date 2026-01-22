#Write a lambda function using filter() which accepts a list of numbers and returns a list of numbers divisible by both 3 and 5.

CheckDivisible=lambda No:(No%3==0 and No%5==0)

def main():
    Data=[1,2,3,4,5,6,7,8,9,10,15]
    print(Data)
    FData=list(filter(CheckDivisible,Data))
    print(FData)

if __name__=="__main__":
    main()