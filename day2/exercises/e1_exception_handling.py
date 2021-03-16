"""
Exercise
The program below crashes. Add exception handling,
so that the program no longer crashes.
"""
database = [
    {"name": "John Doe", "email": "john@doe.com"},
    {"name": "Jennifer Smith", "email": "jsmith@hotmail.com"},
    {"name": "Mr Python"},
]


def main():
    for person in database:
        print(person['email'])


if __name__ == '__main__':
    main()
