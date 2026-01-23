# Write a program which accept N numbers from user and store it into List.Accept one number from user and return frequency of that number from List.
# Input Elements: 13 5 45 7 4 56 5 34 2 5 65
# Input NO=11
# Element to search : 5
# Output:3

def Frequency(Data,No1):
    Size=len(Data)
    Count=0
    for i in range(Size):
        if Data[i]==No1:
            Count=Count+1
    return Count

def main():
    No1=int(input("Enter the number of elements:"))
    No2=int(input("Enter the element to search:"))
    Data=list()
    print("Enter the elements:")
    for i in range(No1):
        Ret=int(input())
        Data.append(Ret)
    Result=Frequency(Data,No2)
    print("The frequency of",No2,"is:",Result)

if __name__=="__main__":
    main()
