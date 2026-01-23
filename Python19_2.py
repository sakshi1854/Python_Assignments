# Write a program which contains one lambda function which accepts two parameters and return its multiplication.
# Input: 4  3             Output:12
# Input: 6   3            Output:18

Multiplication=lambda No1,No2:No1*No2

def main():
    No1=int(input("Enter the first number:"))
    No2=int(input("Enter the second number:"))
    Result=Multiplication(No1,No2)
    print("The multiplication of the number is:",Result)

if __name__=="__main__":
    main()