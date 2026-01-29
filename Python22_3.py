#Write a python program to implement a class named as Arithematic with the following characteristics:
# The class should contain two instance variables:Value1,Value2
#Define a constructor(__init__) that initializes all instances of variables to 0
#Implement the following instance methods.
# Accept() -accepts value for Value1 and Value2 from the user.
# Addition()-returns the addition of Value1 and Value2
# Substraction()- returns the substraction of Value1 and Value2
# Multiplication()- returns the multiplication of Value1 and Value2
# Division()-returns the division of Value2(handle division by zero properly)
# Create multiple objects of the arithematic class and invoke all instance methods.


class Arithematic:
    def __init__(self):
        self.Value1=0
        self.Value2=0
    def Accept(self):
        self.Value1=int(input("Enter the first number:"))
        self.Value2=int(input("Enter the second number:"))
    def Addition(self):
        return self.Value1+self.Value2
    def Substraction(self):
        return self.Value1-self.Value2
    def Multiplication(self):
        return self.Value1*self.Value2
    def Division(self):
        if self.Value2!=0:
            return self.Value1/self.Value2
        else:
            print(f"Cannot Divide by{self.Value2}")

obj1=Arithematic()
obj1.Accept()
Ret=obj1.Addition()
print("The addition is:",Ret)
Ret=obj1.Substraction()
print("The substraction is:",Ret)
Ret=obj1.Multiplication()
print("The multiplication is:",Ret)
Ret=obj1.Division()
print("The division is:",Ret)