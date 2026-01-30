#Write a python program to implement a class named Numbers with the following specifications.
# The class should contain one instance variable.
# Value
# Define a constructor(__init__) that accepts a number from the user and initializeS Value.
# Implement the following methods:
# ChkPrime()-returns true if the number is prime,otherwise returns false.
# ChkPerfect()- returns true if the number is perfect,otherwise returns false.
# Factors()-displays all the factors of the number
# SumFctors()-returns the sum of all factors (you may use this method as  helper in chkperfect() if required)
#Create multiple objects and call all methods


class Numbers:
    def __init__(self):
        self.Value=int(input("Enter the number:"))
    def ChkPrime(self):
        No=self.Value
        if No<=1:
            return False
        for i in range(2,No//2+1):
            if No%i==0:
                return False
        return True
    def Factors(self):
        No=self.Value
        print(f"The factors of {No} are:")
        for i in range(1,No+1):
            if No%i==0:
                print(i,end=" ")
    def SumFactors(self):
        No=self.Value
        Sum=0
        for i in range(1,No):
            if No%i==0:
                Sum=Sum+i
        return Sum
    def ChkPerfect(self):
        No=self.Value
        SumOfFactors=self.SumFactors()
        if SumOfFactors==No:
            return True
        else:
            return False

Obj1=Numbers()
ChkPrime=Obj1.ChkPrime()
if ChkPrime==True:
    print("The number is prime number.")
else:
    print("The number is not prime number.")
Obj1.Factors()
print()
Sum=Obj1.SumFactors()
print("The sum of the factors is:",Sum)
ChkPerfect=Obj1.ChkPerfect()
if ChkPerfect==True:
    print("The number is perfect number.")
else:
    print("The number is not perfect number.")