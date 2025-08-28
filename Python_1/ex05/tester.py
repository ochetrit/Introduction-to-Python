from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey
from PIL import UnidentifiedImageError
path = "landscape.jpg"
try:
    array = ft_load(path)
    ft_invert(array)
    ft_red(array)
    ft_green(array)
    ft_blue(array)
    ft_grey(array)
    print(ft_invert.__doc__)
except FileNotFoundError:
    print(f"\033[1;91mFile '{path}' is not findable.")
except PermissionError:
    print(f"\033[1;91mAccess denied: '{path}'.")
except UnidentifiedImageError:
    print(f"\033[1;91mFile '{path}' is not a valid image")
except KeyboardInterrupt:
    print("\033[1;93m\nProgram has been closed with Ctrl+C.")
except Exception as e:
    print(f"\033[1;91mErreur inattendue : {e}")
