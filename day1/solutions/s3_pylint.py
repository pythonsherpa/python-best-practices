"""
Exercise:
Use 'pylint' to refactor the program below. Install pylint first
from the terminal with the following command:

pip install pylint

Then run:

pylint day1/exercises/e3_pylint.py

Fix all the issues that pylint warns about...

Extra challenge:
Check out the plugin for PyCharm: https://plugins.jetbrains.com/plugin/11084-pylint
"""


def main():
    """Run the program."""
    name = input("What is your name? ")
    greet(name)


def greet(name):
    """Return a full sentence greeting."""
    return f"Hello {name}, how are you?"


def make_percentage(number):
    """Return the number as a percentage."""
    percentage = number / 100
    return f"{percentage}%"


if __name__ == "__main__":
    main()
