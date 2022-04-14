from PIL import Image
from PIL.ImageQt import ImageQt
from PIL.ImageFilter import Kernel, MedianFilter

def applyBoxFilter(img):
    boxFilter = Kernel(size=(3,3), kernel=(1,1,1,1,1,1,1,1,1), scale=9)
    boxImg = img.filter(boxFilter)
    return ImageQt(boxImg)

def applyMedianFilter(img):
    medianFilter = MedianFilter(size=3)
    medianImg = img.filter(medianFilter)
    return ImageQt(medianImg)

def applyWeightedAvgFilter(img):
    weightedAvgFilter = Kernel(size=(3,3), 
                                kernel=(1,2,1,2,4,2,1,2,1), scale=16)
    weightedAvgImg = img.filter(weightedAvgFilter)
    return ImageQt(weightedAvgImg)