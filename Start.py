import os
import sys
from PIL import Image
from PIL.ExifTags import GPSTAGS, TAGS


def main():
    while True:
        output_loc = input("Where do you want to print the output?\n\n1.File\n2.Terminal\n\nInput: ")
        output_loc = int(output_loc) # Conversion from a string (input) to int
        if (output_loc == 1):
            # open = redirect output to the file
            sys.stdout = open("exif_data_extract.txt", "w")
            break
        elif (output_loc == 2):
            for image in pictures:
                with Image.open(image) as im:
                    print(im.getexif())
                    print(im.info)
                    print(im)
                    Image.Image.load(im)
                    print("\n============\n")
            break
        print("Wrong input. Please choose between 1 and 2.")

# Current Working Directory; As of now, it is ../ImgMalwareScaner
cwd = os.getcwd()

# Chdir changes the current path to specified path
os.chdir(os.path.join(cwd, "Pictures"))

pictures = os.listdir()
print(pictures)



main()
