from PIL import Image
from PIL.ImageQt import ImageQt
import numpy as np
import cv2 as cv


def applyCanny(img):
    img = cv.imread(img,0)
    edges = cv.Canny(img,100,200)
    edgesPIL = Image.fromarray(edgesPIL)
    return ImageQt(edgesPIL)

