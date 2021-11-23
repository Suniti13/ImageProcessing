from PIL import Image
import numpy as np
import sys


def grey_level_slicing(img, minLevel, maxLevel, bg):

    new_img = img.point(lambda i: slice_pixel(i, minLevel, maxLevel, bg) )
    return new_img

# px - pixel value
# bg - Retain background ? 1 : 0
def slice_pixel(px, minLevel, maxLevel, bg):
    if px>minLevel and px<maxLevel:
        return 255
    else:
        if bg:
            return px
        else:
            return 0

def main(argv):
    img = Image.open("../Pics/len_original.jpg")
    minLevel = int(argv[0])
    maxLevel = int(argv[1])
    bg = int(argv[2])

    op = grey_level_slicing(img, minLevel, maxLevel, bg)

    op.save('op2.jpg')

main(sys.argv[1:])
    

