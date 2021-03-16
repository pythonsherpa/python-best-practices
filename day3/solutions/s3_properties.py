"""
Exercise 1
Recreate the Person class. Implement a getter so that printing
a person's name always start with a capital letter. The expected behavior is:
marc = Person("marcus")  # note the lowercase 'm'
print(marc.name)         # prints "Marcus"
"""


class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name.capitalize()

    @name.setter
    def name(self, value):
        if len(value) <= 1:
            raise ValueError("The name is too short")
        self._name = value


marc = Person("marcus")  # note the lowercase 'm'
print(marc.name)         # prints "Marcus"
