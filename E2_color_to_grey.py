from PIL import Image
from PIL.ImageQt import ImageQt
import numpy as np

def convert_to_greyscale(img):    
    image_arr = np.array(img)
    r, c = image_arr.shape[0], image_arr.shape[1]

    for i in range(r):
        for j in range(c):
            grey = (0.3*image_arr[i][j][0]) + (0.59*image_arr[i][j][1]) + (0.11*image_arr[i][j][2])
            for k in range(3):
                image_arr[i][j][k] = grey
    
    outputImg = Image.fromarray(image_arr)
    
    return ImageQt(outputImg)
