from PIL.ImageQt import ImageQt

def convert_to_negative(img):
    new_img = img.point(lambda i: 255-i)
    return ImageQt(new_img)
