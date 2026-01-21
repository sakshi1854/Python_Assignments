# Write a program which accepts one character and checks whether it is vowel or consonant.
# Input : a 
# Output : Vowel

def CheckVowel(Ch):
    if Ch=='a' or Ch=='e' or Ch=='i' or Ch=='o' or Ch=='u' or Ch=='A' or Ch=='E' or Ch=='I' or Ch=='O' or Ch=='U':
        print("Vowel")
    else:
        print("Consonant")

def main():
    Ch=input("Enter a character:")
    CheckVowel(Ch)


if __name__=="__main__":
    main()