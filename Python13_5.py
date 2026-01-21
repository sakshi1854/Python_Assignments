# Write a program which accepts marks and displays grade.
# Condition Examples:
# 1] >=75 = Distinction 2] >=60 =First Class 3] >=50 = Second Class 4] <50 = Fail

def DisplayGrade(Marks):
    if Marks>=75:
        print("Distinction")
    elif Marks>=60:
        print("First Class")
    elif Marks>=50:
        print("Second Class")
    elif Marks<50:
        print("Fail")
    else:
        print("Invalid Input")

def main():
    Marks=int(input("Enter the marks:"))
    DisplayGrade(Marks)

if __name__=="__main__":
    main()