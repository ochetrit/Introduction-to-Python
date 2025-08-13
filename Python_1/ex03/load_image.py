from PIL import Image, UnidentifiedImageError
import numpy as np


def ft_load(path: str) -> np.array:
    """Loads an image, prints its format, and its pixels\
 content in RGB format"""
    img = Image.open(path)
    img.load()
    img_array = np.array(img)
    print("\033[1;93mThe shape of the image is: ", img_array.shape)
    return img_array
    return None
