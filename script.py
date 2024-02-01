import os

def sort_files():
    source_dir = "/path/to/files"  # Replace with the actual path to your files

    for filename in os.listdir(source_dir):
        if filename.endswith((".MP4", ".JPG", ".WEBP", ".JPEG", ".JPG", ".PNG")):  # Include other extensions if needed
            year, month, day, *_ = filename.split(" ")[0].split("-")
            target_dir = os.path.join(source_dir, year, month, day)
            os.makedirs(target_dir, exist_ok=True)  # Create nested folders if they don't exist
            try:
                os.rename(os.path.join(source_dir, filename), os.path.join(target_dir, filename))
            except:
                pass

if __name__ == "__main__":
    sort_files()
