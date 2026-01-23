# Write a program which accepts N numbers from user and store it into List. Return addition of all elements from that List.
# Input: Number of elements:6
# Input Elements : 13 5 45 7 4 56
# Output: 130

def Addition(Data):
    Sum=0
    for i in range(len(Data)):
        Sum=Sum+Data[i]
    return Sum

def main():
    No1=int(input("Enter the number:"))
    Data=list()
    print("Enter the elements:")
    for i in range(No1):
        Ret=int(input())
        Data.append(Ret)
    Result=Addition(Data)
    print("Addition of elements in the list are:",Result)
    
if __name__=="__main__":
    main()