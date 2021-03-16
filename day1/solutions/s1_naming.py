"""
Rename the following variables and function names
"""

# 1 - descriptive name
first_name = input("What is your first name? ")

# 2 - snake_case
last_name = "Johnson"

# 3 - snake_case (could even be just "movie")
movie_title = "Pulp Fiction"

# 4 - descriptive name
operating_systems = ["Windows", "Linux", "MacOS"]

# 5 - no abbreviations
actors = ["Tom Hanks", "Brad Pitt", "Johnny Depp"]

# 6 - type can be inferred, no need to add it to the variable name
fruits = ["apple", "banana", "kiwi", "orange"]

# 7 - type can be inferred, no need to add it to the variable name
grades = {"English": 90, "Biology": 80, "Math": 100}


# 8 - snake_case & no abbreviation
def convert_temperature(celcius):
    """Return temperature converted from Celsius to Fahrenheit"""
    fahrenheit = (celcius * 1.8) + 32
    return fahrenheit


# 9 - PascalCase for classes
class ElectricVehicle:

    def __init__(self, brand, battery):
        self.brand = brand
        self.battery = battery
