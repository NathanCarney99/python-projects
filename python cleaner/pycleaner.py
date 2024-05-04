import os
from pathlib import Path
import shutil

source_path = "/Users/nathancarney/Downloads"
target_path = "/Users/nathancarney"


dir_list = os.listdir(source_path)


print("Files and directories in '", source_path, "' :")
# prints all files
# print(dir_list)

mySet = set()

for file in dir_list:
    fileName, fileExt = os.path.splitext(str(file))
    ext = fileExt[1:].capitalize()
    print(ext)
    mySet.add(ext)

# print(mySet)

for item in mySet:
    if os.path.isdir(os.path.join(target_path, str(item))):
        print("Directory already created for\n" + item + "\n")
    else:
        print("No Directory Found for\n", item)
        print("Creating Directory")
        os.makedirs(os.path.join(target_path, str(item)))

x=0

# Iterate over files in the source directory
for filename in os.listdir(source_directory):
    source_path = os.path.join(source_directory, filename)
    
    # Check if the path is a file
    if os.path.isfile(source_path):
        fileName, fileExt = os.path.splitext(filename)
        ext = fileExt[1:].capitalize()
        
        # Create subdirectory based on file extension
        target_subdirectory = os.path.join(target_directory, ext)
        os.makedirs(target_subdirectory, exist_ok=True)
        
        # Construct target file path
        target_path = os.path.join(target_subdirectory, filename)
        
        # Copy file to target directory
        print("Copying:", source_path, "to", target_path)
        shutil.copy(source_path, target_path)
    else:
        print("Skipping:", source_path, "as it is not a file.")


    









