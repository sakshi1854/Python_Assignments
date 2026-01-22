# Write a lambda function using map() which accepts a list on numbers and returns a list of squares of each number.

# def Square(No):
#     return No*No

Square=lambda No:No*No

def main():
    Data=[1,2,3,4,5,6]
    print(Data)
    MData=list(map(Square,Data))
    print(MData)

if __name__=="__main__":
    main()