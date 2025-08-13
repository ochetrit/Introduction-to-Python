from PIL import Image, UnidentifiedImageError
import numpy as np


def ft_load(path: str) -> np.array:
    """Loads an image, prints its format, and its pixels\
 content in RGB format"""
    try:
        img = Image.open(path)
        img.load()
        img_array = np.array(img)
        print("\033[1;93mThe shape of the image is: ", img_array.shape)
        return img_array
    except FileNotFoundError:
        print(f"\033[1;91mFile '{path}' is not findable.")
    except PermissionError:
        print(f"\033[1;91mAccess denied: '{path}'.")
    except UnidentifiedImageError:
        print(f"\033[1;91mFile '{path}' is not a valid image")
    except Exception as e:
        print(f"\033[1;91mErreur inattendue : {e}")
    return None


# from load_image import ft_load

# def main():
#     print("\033[1;94mFile that doesn't exist: ")
#     ft_load("test")
#     print()
#     print("\033[1;94mFile that is not an image: ")
#     ft_load("tester.py")
#     print()
#     print(ft_load("animal.jpeg"))


# if __name__ == "__main__":
#     main()
