import logging
import sys
from os import getenv
from typing import ClassVar

from colorama import Back, Fore, Style

PROJECT_ID = getenv("GCP_PROJECT_ID")
DATASET_ID = getenv("BQ_DATASET_ID")
TABLE_NAME = getenv("BQ_TABLE_NAME")

EMPLOYEE_QUERY = f"""
SELECT EmpPhoneNo, EmpSalary, EmployeeName
FROM `{PROJECT_ID}.{DATASET_ID}.{TABLE_NAME}`
LIMIT 50
"""


class ColoredFormatter(logging.Formatter):
    """Custom Formatter class for colored log messages."""

    COLORS: ClassVar[dict] = {
        "DEBUG": Fore.CYAN,
        "INFO": Fore.GREEN,
        "WARNING": Fore.YELLOW,
        "ERROR": Fore.RED,
        "CRITICAL": Fore.WHITE + Back.RED + Style.BRIGHT,
    }

    def format(self, record):
        """Format the specified record as a colored log message.

        Args:
            record (logging.LogRecord): The log record to be formatted.

        Returns:
            str: The formatted log message with color codes.
        """
        color = self.COLORS.get(record.levelname, "")
        message = super().format(record)

        return f"{color}{message}{Style.RESET_ALL}"


def setup_logger() -> logging.Logger:
    """This function sets up a custom logger.

    Returns:
    - logging.Logger: The custom logger object."""

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Removing any existing handlers
    logger.handlers.clear()

    # Creating a console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.DEBUG)

    # Formatting the log messages
    formatter = ColoredFormatter(
        fmt="[%(asctime)s] [%(levelname)s] - %(message)s",
        datefmt="%d-%b-%y %H:%M:%S",
    )

    # Adding the formatter to the console handler
    console_handler.setFormatter(formatter)

    # Adding the console handler to the logger
    logger.addHandler(console_handler)

    return logger


logger = setup_logger()
