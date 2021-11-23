from PIL.ImageQt import ImageQt

def convert_to_bit_plane_slicing(img, plane):
    img_grey = img.convert('L')
    new_img = img_grey.point(lambda i: int((i & 2**plane)/2**plane))
    new_img = new_img.point(lambda i: 255 if i==1 else 0)

    #new_img = img.point(lambda i: int((i & 2**plane or (255 if plane<6 else 0))
    return ImageQt(new_img)
    