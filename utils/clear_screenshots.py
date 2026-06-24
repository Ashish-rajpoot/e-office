import os
import glob

def clear_screenshots(folder="screenshots"):
    if os.path.exists(folder):
        for file in glob.glob(os.path.join(folder, "*.png")):
            os.remove(file)
    else:
        os.makedirs(folder)

# Call once when your program starts
