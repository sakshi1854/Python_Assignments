# Write a program which accepts radius of circle and prints area of circle.

import math

def CalculateArea(radius):
    Area=math.pi*radius*radius
    return Area

def main():
    radius=float(input("Enter the radius:"))
    Area=CalculateArea(radius)
    print(Area)

if __name__=="__main__":
    main()