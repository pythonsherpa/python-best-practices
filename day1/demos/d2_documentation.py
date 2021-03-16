"""
Demo documentation strings (docstrings)
1) module level docstring
2) function docstring
3) class docstring
Based on PEP 257: https://www.python.org/dev/peps/pep-0257/
"""


def multiply(x, y):
    """Return the product of x and y."""
    return x * y


print(multiply.__name__)
print(multiply.__doc__)


class Rectangle:
    """A class used to represent a rectangle shape."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height


print(Rectangle.__doc__)
print(Rectangle.area.__doc__)
