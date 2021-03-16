"""
Rename the following variables and function names
"""

# 1
var = input("What is your first name? ")

# 2
lastName = "Johnson"

# 3
MovieTitle = "Pulp Fiction"

# 4
l = ["Windows", "Linux", "MacOS"]

# 5
actrs = ["Tom Hanks", "Brad Pitt", "Johnny Depp"]

# 6
list_of_fruits = ["apple", "banana", "kiwi", "orange"]

# 7
grades_dict = {"English": 90, "Biology": 80, "Math": 100}


# 8
def convTemp(celcius):
    """Return temperature converted from Celsius to Fahrenheit"""
    fahrenheit = (celcius * 1.8) + 32
    return fahrenheit


# 9
class electricvehicle:

    def __init__(self, brand, battery):
        self.brand = brand
        self.battery = battery
