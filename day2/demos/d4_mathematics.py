"""
Demo unit testing with pytest

First, install pytest from the terminal with:
pip install pytest

Run from the terminal (project's root folder):
python -m pytest -v

Extra:
Choose Pytest in PyCharm Preferences -> Python Integrated Tools
"""


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def round_up(x: float) -> int:
    rounded = int(x) + int((x > 0) and (x - int(x)) > 0)
    return rounded


# Refactored
def round_up(x: float) -> int:
    import math
    return math.ceil(x)


def hypotenuse():
    ...
