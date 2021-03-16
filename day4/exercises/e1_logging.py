"""
Exercise
Add logging to the program below. The program
uses the new `secrets` module to create a token:
https://docs.python.org/3/library/secrets.html

Implement info messages for every function and
a debug message with the value of the token.
For more information about logging:
https://docs.python.org/3/library/logging.html
"""

import secrets


def main():
    """Run program to email a secret token"""
    token = generate_token()
    email_token(token)


def generate_token():
    """Return a token for password reset"""
    token = secrets.token_hex()
    return token


def email_token(token):
    """Email the token"""
    body = f"The token to reset your password: {token}"
    pass


if __name__ == "__main__":
    main()
