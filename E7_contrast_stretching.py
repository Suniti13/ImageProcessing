from PIL import Image
from PIL.ImageQt import ImageQt
import numpy as np

def contrast_stretching(img):
    img_grey = img.convert('L')
    rmin, rmax = getMinMaxLevel(img_grey)
    new_img = img.point(lambda i: int(255*(i-rmin)/(rmax-rmin)))
    return ImageQt(new_img)

def getMinMaxLevel(img):
    img_arr = np.array(img)
    r, c = img_arr.shape[0], img_arr.shape[1]
    rmin = 255
    rmax = 0

    for i in range(r):
        for j in range(c):
            if img_arr[i][j]<rmin:
                rmin = img_arr[i][j]
            if img_arr[i][j]>rmax:
                rmax = img_arr[i][j]
    return rmin, rmax
