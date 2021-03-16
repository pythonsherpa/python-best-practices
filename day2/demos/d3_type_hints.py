"""
Demo type hints
"""
from typing import Dict, List, Union

a: int = 42
b: float = 2.0
c: bool = True
d: str = "hello world"


def add(x: int, y: int) -> int:
    return x + y


print(add(4, 5))
# print(add(6, "7"))  # warning!


def greet(name: str = None) -> str:
    if name is None:
        name = "World!"
    return "Hello " + name


# print(greet(100))  # warning!
print(greet("Amy"))


e: List[int] = [1, 2, 3]
f: Dict[str, float] = {"location": 4.8, "service": 4.9, "quality": 5.0}
g: Union[int, str] = 1
h: List[Union[int, str]] = [1, 2, "c", "d"]


class MyClass:
    value: int = 42

    def __init__(self) -> None:
        ...

    def add(self, x: int, y: int) -> int:
        return x + y
