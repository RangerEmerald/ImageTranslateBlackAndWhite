from PIL import Image
import numpy as np
import sys


textFile = None
size = []
imageName = None

try:
    if len(sys.argv) < 2:
        raise ValueError("Could not find text file. Format: python3 [this file name] [textfile] [width] [height] <to save image name>(optional). Example: python3 drawImageToByte.py text.txt 200 200")
    elif len(sys.argv) >= 2 and len(sys.argv) <= 3:
        raise ValueError("Size array not right size. Array is [width, height]")

    if len(sys.argv) == 5:
        imageName = sys.argv[4]

    textFile = sys.argv[1]
    size = [int(sys.argv[2]), int(sys.argv[3])]
except Exception as error:
    print("An error has occured ---", error)
else:
    try:
        text = open(textFile, 'r').read()

        data = np.ones((size[1], size[0], 3), dtype=np.uint8)

        pos = 0
        pos2 = 0

        for num in text:
            data[pos][pos2] = 255 if int(num) else 0
            pos2 += 1
            if pos2 > size[0] - 1:
                pos2 = 0
                pos += 1

        image = Image.fromarray(data)
        image.show()

        if imageName:
            if not imageName.endswith(".jpg") and not imageName.endswith(".png"):
                raise ValueError("To save file name does not end with .jpg or .png")
            elif imageName.endswith(".jpg"):
                shouldContinue = input("Do you want to use JPG or PNG? PNG could decrease the file size. (PNG/JPG): ")
                if shouldContinue.lower() == "PNG":
                    imageName = imageName.replace(".jpg", ".png")
                
            image.save(imageName)

            print("Saved image to:", imageName)
    except Exception as error:
        print("An error has occured ---", error)