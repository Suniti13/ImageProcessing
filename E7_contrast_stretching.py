from PIL import Image
import numpy as np

img = Image.open("misc/output_neg_weighted_gray.jpg")
img_hist = img.histogram()
print(img_hist)