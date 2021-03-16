"""
Demo dataclasses
"""


# Example regular class
class RegularClassCustomer:
    """Class for a customer."""

    def __init__(self, name: str, email: str, is_active: bool = False):
        self.name = name
        self.email = email
        self.is_active = is_active


# Example of the regular style class
d1 = RegularClassCustomer("John Doe", "john@doe.com")
print(d1)
d2 = RegularClassCustomer("John Doe", "john@doe.com")
print(d2 == d1)


# Example dataclass
from dataclasses import dataclass


@dataclass
class DataClassCustomer:
    """Class for a customer."""
    name: str
    email: str
    is_active: bool = False  # assign a default value


# Example of the dataclass
d1 = DataClassCustomer("John Doe", "john@doe.com")
print(d1)
d2 = DataClassCustomer("John Doe", "john@doe.com")
print(d2 == d1)
