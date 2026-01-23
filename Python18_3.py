# Write a program which accept N numbers from user and store it into List.Return Minimum number from that List.
# Input: Number of Elements:4
#Input Elements: 13 5 45 7
# Output:5

def Minimum(Data):
    Size=len(Data)
    MinElement=Data[0]
    for i in range(Size):
        if Data[i]<MinElement:
            MinElement=Data[i]
    return MinElement

def main():
    No1=int(input("Enter the number:"))
    Data=list()
    print("Enter the elements:")
    for i in range(No1):
        Ret=int(input())
        Data.append(Ret)
    Result=Minimum(Data)
    print("The Minimum element from the list is:",Result)

if __name__=="__main__":
    main()