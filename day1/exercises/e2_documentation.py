"""
Add 'docstrings' to the following functions and classes.
Follow PEP 257: https://www.python.org/dev/peps/pep-0257/
"""


# 1
def square(n):
    return n * n


# 2
def count_vowels(word):
    # Return the total number of vowels
    number_of_vowels = 0
    for char in word.lower():
        if char in "aeiou":
            number_of_vowels += 1
    return number_of_vowels


# 3
class Dog:
    'A class to represent a dog.'

    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says whoof!")
