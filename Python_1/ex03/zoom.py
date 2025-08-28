from load_image import ft_load
from PIL import UnidentifiedImageError
# import numpy as np
import matplotlib.pyplot as plt


def main():
    path = "animal.jpeg"
    MSG = "\033[1;96mNew shape after slicing: \033[1;97m"
    try:
        array_image = ft_load("animal.jpeg")
        print(array_image)
        array_zoomed = array_image[100:500, 450:850, 0]
        print(MSG, array_zoomed.shape)
        print(array_zoomed)
        plt.imshow(array_zoomed, cmap='gray')
        plt.axis('on')
        plt.show()
    except FileNotFoundError:
        print(f"\033[1;91mFile '{path}' is not findable.")
    except PermissionError:
        print(f"\033[1;91mAccess denied: '{path}'.")
    except UnidentifiedImageError:
        print(f"\033[1;91mFile '{path}' is not a valid image")
    except Exception as e:
        print(f"\033[1;91mErreur inattendue : {e}")
    except KeyboardInterrupt:
        print("\033[1;93m\nProgram has been closed with Ctrl+C.")


if __name__ == "__main__":
    main()
