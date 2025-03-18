
# import the os module to work with files and directories
import os
from pathlib import Path

# pwd - print working directory
print("current working directory:", os.getcwd())

# File paths
TEXT_FILE_NAME = "data.txt" # constant variable (for user to look at)

# One method of joining paths
file_path = os.getcwd() + "/" + TEXT_FILE_NAME

# May not work across all operating systems
# Using os.path.join() is a better way to join paths

file_path = os.path.join(os.getcwd() + '/' + TEXT_FILE_NAME)
print("file path:", file_path)

# Check if a file exists

# ... if os.path.exists(file_path):
# ...     print("file exists")

if (Path.exists(file_path)):
    print("file exists!")
else:
    print("file does not exist")