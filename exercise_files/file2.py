from pathlib import Path

# Get the current working directory
current_dir = Path.cwd()

# Define the text file name
TEXT_FILE_NAME = "demo_files/data.txt"

# Create the full file path
file_path = current_dir / TEXT_FILE_NAME

print(file_path)

# Check if a file exists

# if(os.path.exists(file_path)):
#   print("File exists!")

if (Path.exists(file_path)):
    print("File exists!")
else:
    print("File not found!")

# Make a new directory

Path.mkdir("new_directory", )