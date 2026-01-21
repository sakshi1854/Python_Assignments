# Write a program which accepts length and width of rectangle and prints area.

def CalculateArea(l,w):
    return l*w

def main():
    Length=int(input("Enter the length:"))
    Width=int(input("Enter the width:"))
    Area=CalculateArea(Length,Width)
    print(Area)

if __name__=="__main__":
    main()