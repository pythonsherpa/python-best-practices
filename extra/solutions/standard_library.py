"""
Exercise
All of the functions below are completely unnecessary.
Their functionality was already implemented in the
Standard Library. Replace the function calls on the
last lines of this program with the functions from
the Standard Library.
Use the documentation: https://docs.python.org/3/
Feel free to use search engines as well...
"""
import collections
import math
import statistics


if __name__ == '__main__':
    print(math.ceil(2.4))  # prints 3
    print(statistics.median([823, 934, 877, 540, 700]))  # prints 823
    print(collections.Counter(["john", "jane", "jane", "jessy"]))  # prints {'john': 1, 'jane': 2, 'jessy': 1}
