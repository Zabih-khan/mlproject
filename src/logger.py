import logging
# Import the logging module to handle logging functionality.
import os
# Import the os module to work with operating system-related functions.
from datetime import datetime
# Import the datetime class from the datetime module to work with dates and times.

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# Create a log file name based on the current date and time using the datetime.now() method.

logs_path = os.path.join(os.getcwd(), "logs")
# Create a path for the 'logs' directory using os.getcwd() to get the current working directory.

os.makedirs(logs_path, exist_ok=True)
# Create the 'logs' directory if it doesn't exist using os.makedirs().

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)
# Create the complete path for the log file by joining the 'logs' directory with the log file name.

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
# Set up the logging configuration using logging.basicConfig() to define the log file, format, and log level.



"""
==> logging is useful to track the error and exception or information. 
==> logger.py is used to track events that occure in software when its run. 
==> it is used in developement, debugging, testing etc



"""