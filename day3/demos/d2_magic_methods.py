"""
Demo magic methods
"""
from functools import total_ordering


@total_ordering
class BankAccount:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    # Added later during the demo
    def __str__(self):
        return f"Bank account of {self.owner}"

    # Optional
    def __repr__(self):
        return f'BankAccount("{self.owner}")'

    # Added later during the demo
    def __gt__(self, other):
        return self.balance > other.balance

    # Added later during the demo
    def __eq__(self, other):
        return self.balance == other.balance


# Instantiate and print
account_john = BankAccount("John", 100)
print(account_john)


# Compare two accounts
account_jane = BankAccount("Jane", 100)
print(account_john > account_jane)   # TypeError: '>' not supported

# Compare equal, fix with implementing __eq__()
print(account_john == account_jane)

# Add total_ordering decorator
