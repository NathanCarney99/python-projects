# File Organizer

This Python script helps organize files in a specified directory by creating subdirectories based on file extensions and removing duplicate files.

## Getting Started

To use this script, simply download or clone the repository to your local machine.

### Prerequisites

- Python 3.x
- shutil module (built-in)
- os module (built-in)

### Installation

There is no installation required for this script.

## Usage

1. Modify the `source_path` and `target_path` variables in the script to specify the source directory containing the files to be organized and the target directory where the organized files will be placed.
2. Run the script using Python: `python file_organizer.py`.
3. The script will create directories in the target directory based on unique file extensions found in the source directory.
4. It will then remove duplicate files within each subdirectory of the target directory.
