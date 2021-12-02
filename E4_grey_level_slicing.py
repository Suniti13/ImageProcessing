from PIL import Image
from PIL.ImageQt import ImageQt

def grey_level_slicing(img, minLevel, maxLevel, bg):
    new_img = img.point(lambda i: slice_pixel(i,minLevel,maxLevel,bg))
    return ImageQt(new_img)

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
