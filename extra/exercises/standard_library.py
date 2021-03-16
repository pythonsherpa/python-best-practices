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


def round_up(x: float) -> int:
    rounded = int(x) + int((x > 0) and (x - int(x)) > 0)
    return rounded


def calculate_median(numbers):
    n = len(numbers)
    numbers = sorted(numbers)

    if n % 2 == 0:
        first_number = numbers[n // 2 - 1]
        second_number = numbers[n // 2]
        median = (second_number + first_number) / 2
    else:
        median = numbers[n // 2]
    return median


def counter(iterable):
    counts = {}
    for item in iterable:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts


if __name__ == '__main__':
    print(round_up(2.4))  # prints 3
    print(calculate_median([823, 934, 877, 540, 700]))  # prints 823
    print(counter(["john", "jane", "jane", "jessy"]))  # prints {'john': 1, 'jane': 2, 'jessy': 1}
