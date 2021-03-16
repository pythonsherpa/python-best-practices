"""
Exercise 1
Refactor the code below and make the class "Product" a dataclass

Extra challenge
The dataclass decorator takes a number of arguments, 'eq' and `frozen`.
Learn more about it by reading the docs:
https://docs.python.org/3/library/dataclasses.html
"""
from dataclasses import dataclass


@dataclass
class Product:
    """Class for a product."""
    identifier: int
    name: str
    price: float
    description: str = None

