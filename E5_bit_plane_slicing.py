from PIL.ImageQt import ImageQt

def convert_to_bit_plane_slicing(img, plane):
    img_grey = img.convert('L')
    new_img=img_grey.point(lambda i:[0,255][(i&2**plane)//2**plane==1])
    return ImageQt(new_img)
    