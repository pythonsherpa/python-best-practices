"""
Demo decorators
"""


# Example function
def say_hello():
    print("Hello, how are you?")


# 1. Functions as objects
greet = say_hello
# greet()


# 2. Functions as arguments
def my_simple_decorator(func):
    print("Decorating the function")
    func()


# my_simple_decorator(say_hello)


def my_decorator(func):
    def wrapper():
        print("Before calling the decorated function")
        func()  # this is where the function is called
        print("After calling the decorated function")
    return wrapper


say_hello = my_decorator(say_hello)
say_hello()


@my_decorator
def say_hello():
    print("Hello, how are you?")


@my_decorator
def say_goodbye():
    print("Bye, bye!")


say_hello()
say_goodbye()
