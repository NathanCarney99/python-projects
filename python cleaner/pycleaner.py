import os
import shutil

# Define source and target paths
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

# Remove Duplicates in Target Directories
for dir in mySet:
    sub_folder = os.listdir(os.path.join(target_path, dir))
    
    for file in sub_folder:
        fileName, fileExt = os.path.splitext(str(file))
        ext = fileExt[1:].capitalize()
        
        # Check if the file name has at least 3 characters
        if len(fileName) < 3: continue
        
        # Extracting the last three characters of the file name
        last_Char = fileName[-1]
        sec_Last = fileName[-2]
        third_Last = fileName[-3]
        
        # Form the path to the target file
        target_file = os.path.join(target_path, file)
        
        # Form the path to the target sub-directory based on the file extension
        target_sub_directory = os.path.join(target_path, ext)
        
        # Check for duplicate files (named with a numeric sequence in parentheses)
        if(last_Char == ')' and third_Last == '('):
            if(sec_Last.isnumeric()):
                # Remove duplicate file
                os.remove(os.path.join(target_sub_directory, file))
                print("Duplicate File Removed :", file)
