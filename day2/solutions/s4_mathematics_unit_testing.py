"""
Exercise 1
Install pytest from the terminal with:
pip install pytest

Exercise 2
Run the tests from the terminal (in the project's root folder):
python -m pytest

Extra challenge
Add the test below to the file "day2/demos/test_mathematics.py"
Implement the "hypotenuse" function in the
"day2/demos/d4_mathematics.py" file.
"""


def hypotenuse(a, b):
    """Returns the longest side of a right-angled triangle.

    Pythagorean Theorem: a² + b² = c²

    Args:
        a (int): leg A
        b (int): leg B

    Returns:
        int: hypotenuse (leg C)
    """
    c = (a ** 2 + b ** 2) ** 0.5
    return c


def test_hypotenuse():
    """Returns the longest side of a right-angled triangle.

    Pythagorean Theorem: a² + b² = c²
    3² + 4² = 5²
    9  + 16 = 25
    """
    assert hypotenuse(3, 4) == 5
