"""
Demo classes and instances
"""


# Demo class
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.width * self.length


# Instantiate
my_object = Rectangle(10, 20)

# Print variable
print(my_object.length)

# Use method
print(my_object.area())


# BankAccount
class BankAccount:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def show_balance(self):
        print(f"{self.owner} has USD {self.balance}")


account_john = BankAccount("John")
account_john.deposit(100)
account_john.show_balance()
account_john.withdraw(50)
account_john.show_balance()

account_jessica = BankAccount("Jessica", 500)
account_jessica.deposit(100)
account_jessica.show_balance()
