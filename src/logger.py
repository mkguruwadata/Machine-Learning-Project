import logging  # Import the logging module to log messages
import os  # Import the os module to interact with the operating system
from datetime import datetime  # Import datetime to work with date and time

# Create a log file name with the current date and time (e.g., "08_13_2024_10_30_45.log")
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the path where the log file will be stored
# The log file will be saved in a "logs" directory in the current working directory
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

# Create the "logs" directory if it doesn't exist
os.makedirs(logs_path, exist_ok=True)

# Define the full path to the log file (including the directory and file name)
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure the logging settings
logging.basicConfig(
    filename=LOG_FILE_PATH,  # Set the log file path
    format="[ %(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",  
    # Set the log message format: 
    # - %(asctime)s: Timestamp of the log entry
    # - %(lineno)d: Line number where the log call was made
    # - %(name)s: Logger's name
    # - %(levelname)s: Log level (e.g., INFO, DEBUG, ERROR)
    # - %(message)s: The actual log message
    
    level=logging.INFO,  # Set the logging level to INFO (you can log messages at INFO level or higher)
)
 