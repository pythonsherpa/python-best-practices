"""
Demo context managers
"""
# Good
file = open("zen.txt", "w")
file.write("Simple is better than complex.")
file.close()
print(file.closed)

# Better
file = open("zen.txt", "w")
try:
    file.write("Simple is better than complex.")
finally:
    file.close()
print(file.closed)

# Best
with open("zen.txt", "w") as file:
    file.write("Simple is better than complex")
print(file.closed)


# Demo
class DemoContextManager:
    def __enter__(self):
        print("Entering")

    def __exit__(self, *args):
        print("Exit")


with DemoContextManager():
    print("In the with statement")


# Optional
from contextlib import contextmanager


@contextmanager
def my_open(filename):
    file = open(filename)
    try:
        yield file
    finally:
        file.close()


with my_open("zen.txt") as f:
    for line in f:
        print(line.rstrip())
