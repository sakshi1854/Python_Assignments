# Write a program which accepts one number and checks whether it is perfect number or not.
# Input : 6
# Output : Perfect Number

def CheckPerfect(No1):
    Num=No1
    Sum=0
    for i in range(1,No1):
        if No1%i==0:
            Sum=Sum+i
    if Sum==Num:
        print("Perfect Number")
    else:
        print("Not a Perfect Number")

def main():
    No1=int(input("Enter the number:"))
    CheckPerfect(No1)

if __name__=="__main__":
    main()