# Write a program which accepts name from user and display length of its name.
# Input : Marvellous        Output:10

def PrintLength(Name):
    print(len(Name))

def main():
    Name=input("Enter the string:")
    PrintLength(Name)

if __name__=="__main__":
    main()