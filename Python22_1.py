# Write a python program to implement a class named Demo with the following specifications:
# The class should contain two instance variables:no1 and no2.
# The class should contain one class variable named Value.
# Define a constructor (__init__) that accepts two parameters and initializes the instance variables.
#Implement two instance methods:
# Fun() -displays the values of instance variables no1 and no2.
# Gun() -displays the values of instance variables no1 and no2.
# Create two object of Demo class as follows:
# Obj1=Demo(11,21)
#Obj2=Demo(51,101)
#Call the instance methos in given sequance:
#obj1.Fun()
#obj2.Fun()
#obj1.Gun()
#obj2.Gun()

class Demo:
    Value=10
    def __init__(self,Value1,Value2):
        self.no1=Value1
        self.no2=Value2
    
    def fun(self):
        print("Inside the fun method:",self.no1,self.no2)
    def gun(self):
        print("Inside the gun method:",self.no1,self.no2)

Obj1=Demo(11,21)
Obj2=Demo(51,101)
Obj1.fun()
Obj2.fun()
Obj1.gun()
Obj2.gun()