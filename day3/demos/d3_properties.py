"""
Demo properties
"""


# Example
class Person:
    def __init__(self, name):
        self.name = name


person = Person("Daniel")
# person = Person("D")
print(person)


# Implement getter/setter
class Person:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self._name

    def set_name(self, value):
        if len(value) <= 1:
            raise ValueError("The name is too short")
        self._name = value

    name = property(get_name, set_name)  # important!


person = Person("Daniel")
# person = Person("D")
print(person)


# Pythonic implementation
class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) <= 1:
            raise ValueError("The name is too short")
        self._name = value


person = Person("Daniel")
# person = Person("D")
print(person)
