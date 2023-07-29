from src.logger import logging
# Import the sys module to access system-related functions and variables.
import sys

# Function to format the error message with filename, line number, and error message.
def error_message_detail(error, error_detail: sys):

    # Extract the traceback information from error_detail using exc_info().
    _, _, exc_tb = error_detail.exc_info()

    # Get the filename of the Python script where the exception occurred.
    file_name = exc_tb.tb_frame.f_code.co_filename

    # Create the formatted error message.
    error_message = "Error occurs in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    # Return the formatted error message.
    return error_message

# Custom Exception class that inherits from the built-in Exception class.
class CustomException(Exception):

    # Constructor method for the CustomException class.
    def __init__(self, error_message, error_detail: sys):

        # Set the error message.
        super().__init__(error_message)

        # Create a more detailed error message.
        self.error_message = error_message_detail(
            error_message, error_detail=error_detail)

    # The __str__ method for the CustomException class.
    def __str__(self) -> str:

        # Return the detailed error message when the CustomException instance is converted to a string.
        return self.error_message
