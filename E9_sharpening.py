from PIL import Image
from PIL.ImageQt import ImageQt
from PIL.ImageFilter import Kernel, MedianFilter
import numpy as np

def applyLaplacianFilter(img):
    laplacianFilter = Kernel(size=(3,3), 
        kernel=(-1,-1,-1,-1,8,-1,-1,-1,-1), scale=1)
    laplacianImg = img.filter(laplacianFilter)
    return ImageQt(laplacianImg)

def applySobelFilter(img):
    horizontalFilter = Kernel((3,3), (-1,0,1,-2,0,2,-1,0,1), 1)
    verticalFilter = Kernel((3,3), (-1,-2,-1,0,0,0,1,2,1), 1)
    horizontalGrad = img.filter(horizontalFilter)
    verticalGrad = img.filter(verticalFilter)
    npHorz = np.asarray(horizontalGrad).astype('float')
    npVert = np.asarray(verticalGrad).astype('float')
    npEdge = np.sqrt( npHorz*npHorz + npVert*npVert )
    edgeGrad = Image.fromarray(npEdge.astype('uint8'))
    return ImageQt(edgeGrad)

def applyPrewittFilter(img):
    horizontalFilter = Kernel((3,3), (-1,0,1,-1,0,1,-1,0,1), 1)
    verticalFilter = Kernel((3,3), (-1,-1,-1,0,0,0,1,1,1), 1)
    horizontalGrad = img.filter(horizontalFilter)
    verticalGrad = img.filter(verticalFilter)
    npHorz = np.asarray(horizontalGrad).astype('float')
    npVert = np.asarray(verticalGrad).astype('float')
    npEdge = np.sqrt( npHorz*npHorz + npVert*npVert )
    edgeGrad = Image.fromarray(npEdge.astype('uint8'))
    return ImageQt(edgeGrad)