"""
Demo generators
"""
# iterable
for x in [1, 2, 3]:
    print(x)


# Infinite counter (Iterator)
class MyCounter:
    def __init__(self, value=0):
        self.value = value

    def __iter__(self):
        return self

    def __next__(self):
        value = self.value
        self.value += 1
        return value


counter = MyCounter()
print(next(counter))
print(next(counter))


def my_generator():
    a = "Going first"
    yield a  # stops here first
    b = "Going second"
    yield b


gen = my_generator()
print(next(gen))
print(next(gen))
print(next(gen))

for x in my_generator():
    print(x)


# Infinite counter (generator)
def my_counter(n=0):
    while True:
        yield n
        n += 1


counter = my_counter()
print(next(counter))
print(next(counter))


# Optional
import sys
list_comp = [x for x in range(1000000)]
generator = (x for x in range(1000000))
print(sys.getsizeof(list_comp))
print(sys.getsizeof(generator))
