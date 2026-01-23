# Write a program which contains one lambda function which accepts one parameter and return power of two.
# Input:4     Output:16
# Input:6     Output:36

Power=lambda No1:No1**2

def main():
    No1=int(input("Enter the number:"))
    Result=Power(No1)
    print(Result)

if __name__=="__main__":
    main()