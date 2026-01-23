# Write a program which accept N numbers from user and store it into List.Return Maximum number from that List.
# Input: Number of elements:7
# Input Elements: 13 5 45 7 4 56 34
# Output:56

def Maximum(Data):
    Size=len(Data)
    MaxElement=Data[0]
    for i in range(Size):
        if Data[i]>MaxElement:
            MaxElement=Data[i]
    return MaxElement

def main():
    No1=int(input("Enter the number:"))
    Data=list()
    print("Enter the element:")
    for i in range(No1):
        Ret=int(input())
        Data.append(Ret)
    Result=Maximum(Data)
    print("The maximum element from the list is:",Result)

if __name__=="__main__":
    main()