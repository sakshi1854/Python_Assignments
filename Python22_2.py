#Write a program to implement a class named as Circle with the following requirements.
# The class should contain three instance variables: Radius,Area and Circumference.
#The class should contain one class variable named as PI,initialized to 3.14.
# Define a constructor(__init__) that initializes all instance variable with 0.0
#Implement the following instance methods.
#Accept()- accepts the radius of circle from the user.
# CalculateArea()-calculates the area of the circle and stores it in the Area variable.
# CalculateCircumferece()-calculates the circumference of the circle and stores it in the circumference variable.
# Display()- displays the values of Radius,Area and Circumeference.
#Create multiple objects of circle class and invoke all the instance method for each object.

class Circle:
    PI=3.14
    def __init__(self):
        self.Radius=0.0
        self.Area=0.0
        self.Circumference=0.0
    def Accept(self):
        self.Radius=int(input("Enter the radius of the circle:"))
    def CalculateArea(self):
        self.Area=Circle.PI*self.Radius*self.Radius
    def CalculateCircumference(self):
        self.Circumference=2*Circle.PI*self.Radius
    def Display(self):
        print("The Radius of the circle is:",self.Radius)
        print("The Area of the circle is:",self.Area)
        print("The circumference of circle is:",self.Circumference)

obj1=Circle()
obj1.Accept()
obj1.CalculateArea()
obj1.CalculateCircumference()
obj1.Display()