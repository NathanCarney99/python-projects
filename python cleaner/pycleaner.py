import os
import shutil

source_path = "/Users/nathancarney/Downloads"
target_path = "/Users/nathancarney"

# Get a list of files in the source directory
dir_list = os.listdir(source_path)

# Create a set to store unique file extensions
mySet = set()

# Extract file extensions and add them to the set
for file in dir_list:
    fileName, fileExt = os.path.splitext(str(file))
    ext = fileExt[1:].capitalize()
    mySet.add(ext)

# Create directories based on unique file extensions
for item in mySet:
    if not os.path.isdir(os.path.join(target_path, str(item))):
        print("Creating Directory for", item)
        os.makedirs(os.path.join(target_path, str(item)))

# Iterate over files in the source directory
for filename in os.listdir(source_path):
    source_file_path = os.path.join(source_path, filename)
    
    # Check if the path is a file
    if os.path.isfile(source_file_path):
        fileName, fileExt = os.path.splitext(filename)
        ext = fileExt[1:].capitalize()
        
        # Create subdirectory based on file extension
        target_subdirectory = os.path.join(target_path, ext)
        
        # Construct target file path
        target_file_path = os.path.join(target_subdirectory, filename)
        
        # Check if target file already exists
        if not os.path.exists(target_file_path):
            # Copy file to target directory
            print("Copying:", source_file_path, "to", target_file_path)
            shutil.copy(source_file_path, target_file_path)
        else:
            print("File", filename, "already exists in", target_subdirectory)
    else:
        print("Skipping:", source_file_path, "as it is not a file.")
