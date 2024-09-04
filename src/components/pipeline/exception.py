import sys  # Importing the sys module to access system-specific parameters and functions
from logger import logging

# The error_message_detail function extracts the file name and line number where the error occurred, along with the error message itself.
def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()  # Get the traceback object
    file_name = exc_tb.tb_frame.f_code.co_filename  # Get the name of the file where the error occurred
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)  # Create the error message string with file name, line number, and error message
    )
    return error_message  # Return the detailed error message

# CustomException class is designed to create a more descriptive exception, which includes details about where the error occurred in the code.
class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):  # Initialize the custom exception class with the actual error and error details
        super().__init__(error_message)  # Call the parent class (Exception) constructor with the error message
        self.error_message = error_message_detail(error_message, error_detail=error_detail)  # Store a detailed error message with additional context

    def __str__(self):
        return self.error_message  # Define what to return when the exception is printed: the detailed error message


