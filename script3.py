import os
import shutil

# Define the root directory where your folders are located
root_dir = "/path/to/files"

# Function to create directories based on the folder names
def organize_folders(root_dir):
    # Get a list of all folders in the root directory
    folders = os.listdir(root_dir)
    
    # Traverse through each folder
    for folder in folders:
        if os.path.isdir(os.path.join(root_dir, folder)):
            # Extract year, month, and day from the folder name
            year, month, day = folder.split("-")
            
            # Create directory structure
            year_dir = os.path.join(root_dir, year)
            month_dir = os.path.join(year_dir, month)
            day_dir = os.path.join(month_dir, day)
            
            # Create directories if they don't exist
            if not os.path.exists(year_dir):
                os.mkdir(year_dir)
            if not os.path.exists(month_dir):
                os.mkdir(month_dir)
            if not os.path.exists(day_dir):
                os.mkdir(day_dir)
            
            # Move the folder into the appropriate directory
            src_folder = os.path.join(root_dir, folder)
            dest_folder = day_dir
            shutil.move(src_folder, dest_folder)
            print(f"Moved {folder} to {dest_folder}")

# Call the function to organize the folders
organize_folders(root_dir)
