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

new_dir = current_dir / "new_directory"
new_dir.mkdir(exist_ok=True)
# prevent any errors if the directory already exists


# Opening a file

# Opening a file with a context manager
with open(file_path) as file:
    # Do stuff with the file contents
    print(file.read())

print(file)
# context manager automatically closes the file
# when the block of code is exited - no more reads allowed
# print(file.read())  



# Way of doing withoout context manager
# not good practice
opened_file = open(file_path)
print(opened_file.read())
opened_file.close()

print(opened_file)

