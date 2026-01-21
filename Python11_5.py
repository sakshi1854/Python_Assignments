# Write a program which accepts one number and checks whether it is palindrome or not.
# Input: 121
# Output: Palindrome

def CheckPalindrome(No1):
    Rev=0
    Num=No1
    while Num!=0:
        Digit=Num%10
        Rev=(Rev*10)+Digit
        Num=Num//10
    if No1==Rev:
        print("It is Palindrome")
    else:
        print("It is not Palindrome")

def main():
    No1=int(input("Enter the number:"))
    CheckPalindrome(No1)

if __name__=="__main__":
    main()