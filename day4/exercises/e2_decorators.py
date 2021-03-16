"""
Complete the code snippet below. You need to implement a timer decorator
that prints the total run time of a function. The output should resemble
the expected behavior below (with a different value for the seconds of
course, because that is depending on the computer on which you run it).

*Optional extra challenge*: use wraps from the functools module:
https://docs.python.org/3/library/functools.html#functools.wraps
"""


# Exercise
import time


def timer(func):
    def wrapper():
        """YOUR CODE"""
        ...
    return wrapper


@timer
def do_something():
    """Toy function to keep Python busy"""
    "-".join(str(n) for n in range(10000))
    print("Doing something...")


do_something()  # prints  "Run time was 0.00030457 seconds."
