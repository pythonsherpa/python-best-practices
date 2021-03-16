"""
Demo standard library
"""
import math
import statistics

# Floor (manually)
n = 4.6
n = str(n)
print(n[0])

# With math
print(math.floor(4.6))

# Mean
sales = [100, 95, 120, 135, 140, 80, 70, 75]
total = sum(sales)
count = len(sales)
print(total / count)

# With statistics
print(statistics.mean(sales))
