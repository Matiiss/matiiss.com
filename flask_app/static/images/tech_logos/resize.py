from PIL import Image
import glob, os

size = 70, 70

for infile in glob.glob("*.png"):
    file, ext = os.path.splitext(infile)
    if file.endswith("_original"):
        os.rename(file + ext, file.replace("_original", "") + ext)
    else:
        os.remove(file + ext)
