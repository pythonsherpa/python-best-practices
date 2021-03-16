"""
Demo logging

Levels:
- critical
- error
- warning
- info
- debug
"""
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)-8s %(message)s",
    filename="logging_demo.log",
    filemode="a"
)


def main():
    logging.info("Starting the program")
    retrieve_data()
    store_data()
    logging.info("Ending the program")


def retrieve_data():
    logging.info("Downloading data")
    # do stuff
    data = [1, 2, 3]
    logging.debug(data)


def store_data():
    logging.info("Storing data")
    # do stuff
    ...


if __name__ == '__main__':
    main()
