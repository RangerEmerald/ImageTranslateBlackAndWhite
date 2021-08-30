import cv2
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import sys
import os
import tempfile

fileName = "blackandwhite.txt"
debug = False

try:
    if len(sys.argv) < 2:
        raise ValueError("Could not find file name to convert. File name should be argument. Format: python3 [this file] [jpg to convert] <end file name>(optional)")

    if len(sys.argv) >= 3:
        fileName = sys.argv[2]

    if len(sys.argv) >= 4:
        debug = sys.argv[3]

    fd, path = tempfile.mkstemp(suffix='.png')

    image_file = Image.open(sys.argv[1])
    image_file = image_file.convert('1')
except Exception as error:
    print("An error has occured ---", error)
else:
    try:
        image_file.save(path)
    except Exception as error:
        print("An error has occured ---", error)
    else: 
        image = cv2.imread(path, 0)
        img_reverted = cv2.bitwise_not(image)
        new_img = img_reverted / 255.0

        if debug:
            np.savetxt(debug, new_img)

        print("Image dimensions:", new_img.shape, " | (height by width)")

        string = ""

        for arr in new_img:
            for num in arr:
                if num > 0.75:
                    string += "0"
                else:
                    string += "1"

        with open(fileName, "w") as txtFile:
            txtFile.write(string)

        print("File name:", fileName)
        print("Finished.")
    finally:
        os.remove(path)
