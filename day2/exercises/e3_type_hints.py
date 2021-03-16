"""
Exercise
Add type hints to the code below and catch the bug.
"""


def main():
    """Simple program for illustrative purposes"""
    age = ask_user_age()
    print_age(age)


def ask_user_age():
    """Return user input"""
    age = input("What is your age in years? ")
    return age


def print_age(age):
    """Print full sentence"""
    age_in_months = age * 12
    print(f"You are {age_in_months} months old.")


if __name__ == "__main__":
    main()
