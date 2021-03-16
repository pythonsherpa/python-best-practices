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
import logging
import secrets

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)-8s %(message)s",
    # filename="logging_exercise.log",
    # filemode="w"
)


def main():
    """Run program to email a secret token"""
    logging.info("Start program")
    token = generate_token()
    email_token(token)
    logging.info("End program")


def generate_token():
    """Return a token for password reset"""
    logging.info("Generating token")
    token = secrets.token_hex()
    logging.debug(f"Token: {token}")
    return token


def email_token(token):
    """Email the token"""
    logging.info("Emailing the token")
    body = f"The token to reset your password: {token}"
    pass


if __name__ == "__main__":
    main()
