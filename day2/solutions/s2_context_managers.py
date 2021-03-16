"""
Exercise
Refactor the program below (use a "with" statement).

Extra challenge:
Create a context manager yourself. Try some variations
on the context manager from the demo.

Extra (difficult) challenge:
Create a context manager for a database connection.
The following article has a nice example:
https://www.geeksforgeeks.org/context-manager-in-python/
"""


def main():
    text = "Explicit is better than implicit."
    write_to_file(text)


def write_to_file(text):
    with open("exercise.txt", "w") as f:
        f.write(text)


if __name__ == "__main__":
    main()
