from datetime import datetime
import os
import shutil
import sys, getopt


def fileOrganizer(photosPath):
    mediaExtens = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.mp4', '.avi', '.mkv', '.mov']
    files = os.listdir(photosPath)
    # List of valid media file extensions
    for file in files:
        filePath = os.path.join(photosPath, file)
        # Check file extension
        if any(file.lower().endswith(ext) for ext in mediaExtens):
            # Get the modification date
            modificationTime = os.path.getmtime(filePath)
            modificationDate = datetime.fromtimestamp(modificationTime)
            # Create a folder based on the modification date
            newFoldername = modificationDate.strftime('%Y-%m-%d')
            newFolderPath = os.path.join(photosPath, newFoldername)
            # Check if the folder before creating it
            if not os.path.exists(newFolderPath):
                print('Folder ' + newFolderPath + ' created.')
                os.makedirs(newFolderPath)
            # Move the media file to the corresponding folder
            new_file_path = os.path.join(newFolderPath, file)
            shutil.move(filePath, new_file_path)
    print("Files have been organized.")


def main(argv):
   opts, args = getopt.getopt(argv,"hi:o:",["iphotopath="])
   for opt, arg in opts:
      if opt == '-h':
         print ('photoOrganizer -i path-to-folder-with-photos')
         sys.exit()
      elif opt in ("-i", "--iphotopath"):
         iphotopath = arg
         print ('Organizing files inside:', iphotopath)
         fileOrganizer(iphotopath)

if __name__ == "__main__":
   main(sys.argv[1:])