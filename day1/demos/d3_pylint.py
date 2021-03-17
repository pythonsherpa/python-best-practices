"""
Demo of pylint. Install it first via the terminal with:
pip install pylint

Run from terminal:
pylint day1/demos/d3_pylint.py

Different types of messages :
  * (C) convention, for programming standard violation
  * (R) refactor, for bad code smell
  * (W) warning, for python specific problems
  * (E) error, for much probably bugs in the code
  * (F) fatal, if an error occurred which prevented pylint from processing.
"""


def convertEur2Usd(amount):
   amount * 1.20
   return result


if __name__ == '__main__':
    print(convertEur2Usd(500))
