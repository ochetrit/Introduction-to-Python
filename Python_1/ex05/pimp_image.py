import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array: np.array) -> np.array:
    """Inverts the color of the image received."""
    print(array)
    inverted = 255 - array
    plt.imshow(inverted)
    plt.axis('off')
    plt.show()
    return inverted


def ft_red(array: np.array) -> np.array:
    """Apply a red filter on the image received"""
    print(array)
    red_arr = array.copy()
    red_arr[:, :, 1:] = 0
    plt.imshow(red_arr)
    plt.axis('off')
    plt.show()
    return red_arr


def ft_green(array: np.array) -> np.array:
    """Apply a green filter on the image received"""
    print(array)
    green_arr = array.copy()
    green_arr[:, :, [0, 2]] = 0
    plt.imshow(green_arr)
    plt.axis('off')
    plt.show()
    return green_arr


def ft_blue(array: np.array) -> np.array:
    """Apply a blue filter on the image received"""
    print(array)
    blue_arr = array.copy()
    blue_arr[:, :, :2] = 0
    plt.imshow(blue_arr)
    plt.axis('off')
    plt.show()
    return blue_arr


def ft_grey(array: np.array) -> np.array:
    """Apply a grey filter on the image received"""
    print(array)
    grey_arr = array.mean(axis=-1)
    arr = grey_arr.astype(np.uint8)
    plt.imshow(arr, cmap='gray')
    plt.axis('off')
    plt.show()
    return arr


# from load_image import ft_load
# from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey
# from PIL import UnidentifiedImageError
# path = "landscape.jpg"
# try:
#     array = ft_load(path)
#     ft_invert(array)
#     ft_red(array)
#     ft_green(array)
#     ft_blue(array)
#     ft_grey(array)
#     print(ft_invert.__doc__)
# except FileNotFoundError:
#     print(f"\033[1;91mFile '{path}' is not findable.")
# except PermissionError:
#     print(f"\033[1;91mAccess denied: '{path}'.")
# except UnidentifiedImageError:
#     print(f"\033[1;91mFile '{path}' is not a valid image")
# except KeyboardInterrupt:
#     print("\033[1;93m\nProgram has been closed with Ctrl+C.")
# except Exception as e:
#     print(f"\033[1;91mErreur inattendue : {e}")
