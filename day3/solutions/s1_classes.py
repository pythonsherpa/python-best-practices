"""
Exercise 1.
Create a new class called "Person", with two variables: name & age.
When you have created your class, you should be able to use it as follows:
p1 = Person("John", 42)
print(p1.name)
print(p1.age)

# Exercise 2
Implement a method called "say_hello()".
You should be able to use it as follows:
p1 = Person("John", 42)
p1.say_hello()  # prints "John says hello"
"""


# Exercise 1
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("John", 42)
print(p1.name)
print(p1.age)


# Exercise 2
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"{self.name} says hello!")


p2 = Person("Jane", 42)
p2.say_hello()
