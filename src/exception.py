import logging
import sys
# Import the sys module to access system-related functions and variables.

def error_message_detail(error, error_detail: sys):
    # Function to format the error message with filename, line number, and error message.

    _, _, exc_tb = error_detail.exc_info()
    # Extract the traceback information from error_detail using exc_info().

    file_name = exc_tb.tb_frame.f_code.co_filename
    # Get the filename of the Python script where the exception occurred.

    error_message = "Error occurs in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    # Create the formatted error message.

    return error_message
    # Return the formatted error message.

class CustomException(Exception):
    # Custom Exception class that inherits from the built-in Exception class.

    def __init__(self, error_message, error_detail: sys):
        # Constructor method for the CustomException class.

        super().__init__(error_message)
        # Set the error message.

        self.error_message = error_message_detail(error_message, error_detail=error_detail)
        # Create a more detailed error message.

    def __str__(self) -> str:
        # The __str__ method for the CustomException class.

        return self.error_message
        # Return the detailed error message when the CustomException instance is converted to a string.

        
