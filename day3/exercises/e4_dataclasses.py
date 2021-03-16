"""
Exercise 1
Refactor the code below and make the class "Product" a dataclass

Extra challenge
The dataclass decorator takes a number of arguments, 'eq' and `frozen`.
Learn more about it by reading the docs:
https://docs.python.org/3/library/dataclasses.html
"""
from dataclasses import dataclass


class Product:
    """Class for a product."""
    def __init__(self, identifier: str, name: str, price: float, description: str = None):
        self.identifier = identifier
        self.name = name
        self.description = description
        self.price = price
