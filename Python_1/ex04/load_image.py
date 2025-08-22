from PIL import Image
import numpy as np


def ft_load(path: str) -> np.array:
    """Loads an image, prints its format, and its pixels\
 content in RGB format"""
    img = Image.open(path)
    img.load()
    img_array = np.array(img)
    print("\033[1;96mThe shape of the image is: \033[1;97m", img_array.shape)
    return img_array
