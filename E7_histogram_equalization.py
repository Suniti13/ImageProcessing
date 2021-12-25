from PIL import Image
from PIL.ImageQt import ImageQt
import numpy as np
import matplotlib.pyplot as plt


def generate_histogram(img):
    ''' Take PIL.Image, Return np img histogram array '''    
    img_grey = img.convert('L')
    img_hist = np.array(img_grey.histogram())
    return img_hist

def plot_histogram(initial_hist, final_hist):
    plt.subplot(1,2,1)
    plt.bar(range(256), initial_hist)
    plt.title("Initial Histogram")

    plt.subplot(1,2,2)
    plt.bar(range(256), final_hist)
    plt.title("Final Histogram")

    plt.show()

def histogram_eq(pil_img):
    img_hist_arr = generate_histogram(pil_img)
    sum_nk = np.cumsum(img_hist_arr)
    sum_pk = sum_nk/sum_nk[-1]
    sk = np.round(sum_pk*255)
    eq_img = pil_img.point(lambda i: int(sk[i]))

    new_img_hist_array = generate_histogram(eq_img)

    return ImageQt(eq_img),img_hist_arr, new_img_hist_array

