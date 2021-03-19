"""
Demo exception handling
"""

# ZeroDivision
try:
    print(1 / 0)
except ZeroDivisionError:
    print("Not possible to divide by zero")


# Ask for user input without exception handling
number = input("Give me a number please ")
print(number * 2)   # string!
# Ask again, cast to integer. Error if user answers with text.
number = int(input("Give me a number please "))
print(number * 2)


# Exception handling (bare except)
try:
    number = int(input("Give me a number please "))
    print(100 / number)
except:
    print("Not a valid number")


# Ask for user input with exception handling
try:
    number = int(input("Give me a number please "))
    print(100 / number)
except ValueError:
    print("That was not a valid number")
except ZeroDivisionError:
    print("Not possible to divide by zero")


# Finally
try:
    print(1 / 0)
except ZeroDivisionError:
    print("Not possible to divide by zero")
finally:
    print("Goodbye, end of the program")


# Extra
class NegativeNumberError(Exception):
    """Custom exception for negative numbers"""


try:
    number = int(input("Give a number please "))
    if number < 0:
        raise NegativeNumberError
except NegativeNumberError:
    print("Number cannot be negative")
