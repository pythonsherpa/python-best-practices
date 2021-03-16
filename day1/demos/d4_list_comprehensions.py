"""
Demo of list comprehensions
"""
from day1.demos.d1_naming import convert_eur_to_usd

numbers_squared = []
for x in range(5):
    numbers_squared.append(x ** 2)

print(numbers_squared)

# List comprehension
numbers_squared = [x ** 2 for x in range(5)]
print(numbers_squared)


prices_eur = [100, 80, 95, 200]
prices_usd = [convert_eur_to_usd(price) for price in prices_eur]
print(prices_usd)


# Extra: dictionary comprehensions
# Example 1
squares = {}
for n in range(1, 5):
    squares[n] = n ** 2
print(squares)  # prints {1: 1, 2: 4, 3: 9, 4: 16}

# Dict comprehension
squares = {x: x ** 2 for x in range(1, 5)}
print(squares)  # prints {1: 1, 2: 4, 3: 9, 4: 16}


# Example 2
employees = {"john": 1234, "claire": 1235, "danny": 1236}
employees = {v: k for k, v in employees.items()}
print(employees)
