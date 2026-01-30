#Write a python program to implement a class named BankAccount with the following requirements.
# The class should contain two instance variables.
#Name (Account Holder name)
#Amount(Account balance)
#The class should contain one class variable.
#ROI (Rate of Interese),initialized to 10.5
#Define a constructor(__init__) that accepts Name and initial Amount
# Implement the following instance method.
# Display()-displays account holder name and current balance
#Deposit()-accepts an amount from the user and add it to balance.
# Withdraw()-acceots the amount from the user and substracts it from balance (Ensure withdrawal is allowed only if sufficient balance exists)
#CalculateInterest()-Calculates and returns interest using the formula:
#Interest=(Amount*ROI)/100
#Create multiple objects and demonstrates all methods.

class BankAccount:
    ROI=10.5
    def __init__(self,Name,Amount):
        self.Name=Name
        self.Amount=Amount
    def Display(self):
        print(f"The Account holder name is:{self.Name} and the current balance is:{self.Amount}")
    def Deposit(self):
        Money=int(input("Enter the money to deposit:"))
        self.Amount=self.Amount+Money
    def Withdraw(self):
        Money1=int(input("Enter the amount for withdrawal:"))
        if Money1>self.Amount:
            print("Insufficient Balance for Withdrawal.")
        else:
            self.Amount=self.Amount-Money1
    def CalculateInterest(self):
        Interest=(self.Amount*BankAccount.ROI)/100
        return Interest

Obj1=BankAccount("Sakshi Choudhari",10000)
Obj1.Display()
Obj1.Deposit()
Obj1.Display()
Obj1.Withdraw()
Obj1.Display()
Interest=Obj1.CalculateInterest()
print("The interest is:",Interest)