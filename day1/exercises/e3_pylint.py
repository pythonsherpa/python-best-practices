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
import statistics, os


def main():
   name = input("What is your name? ")
   greet(name)


def greet(name):
    local_variable = 42
    print(f"Hello %s, how are you?" % name);
    return

def make_percentage():
    percentage = number / 100
    pass
    return f"{percentage}%"


if __name__ == "__main__":
    main()
