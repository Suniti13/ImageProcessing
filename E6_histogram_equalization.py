from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def generate_histogram(img):
    ''' Take PIL.Image, Return np img histogram array '''
    
    img_grey = img.convert('L')
    img_hist = np.array(img_grey.histogram())
    return img_hist

def plot_histogram(img_hist_arr):
    fig, ax = plt.subplots()
    ax.bar(range(256), img_hist_arr)
    ax.set(xlim=(0, 255))

    plt.show()

def histogram_eq(pil_img):
    img_hist_arr = generate_histogram(pil_img)
    sum_nk = np.cumsum(img_hist_arr)
    sum_pk = sum_nk/sum_nk[-1]
    sk = np.round(sum_pk*255)
    eq_img = pil_img.point(lambda i: sk[i])
    eq_img.show()

    new_img_hist_array = generate_histogram(eq_img)

    plot_histogram(img_hist_arr)
    plot_histogram(new_img_hist_array)


img = Image.open("../Pics/len_original.jpg")
histogram_eq(img)
