# 04. Create a specific subdirectory and copy one file from another subdirectory to this newly created subdirectory

import os
import shutil

# Define source and destination paths
source_file = "/path/to/source_directory/filename.txt"
destination_dir = "/path/to/target_directory/new_folder"

# Create the new subdirectory if it doesn't exist
os.makedirs(destination_dir, exist_ok=True)

# Copy the file
shutil.copy(source_file, destination_dir)
print("✅ File Copied!")