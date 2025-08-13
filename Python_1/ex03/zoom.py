from load_image import ft_load
from PIL import Image, UnidentifiedImageError
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

def main():
    try:
        print(matplotlib.get_backend())
        array_image = ft_load("animal.jpeg")
        array_zoomed = array_image[200:600, 200:600, 0]
        # plt.imshow()(array_zoomed, cmap = 'gray')
        # plt.axis('off')
        # plt.show()
    except FileNotFoundError:
        print(f"\033[1;91mFile '{path}' is not findable.")
    except PermissionError:
        print(f"\033[1;91mAccess denied: '{path}'.")
    except UnidentifiedImageError:
        print(f"\033[1;91mFile '{path}' is not a valid image")
    except Exception as e:
        print(f"\033[1;91mErreur inattendue : {e}")


if __name__ == "__main__":
    main()