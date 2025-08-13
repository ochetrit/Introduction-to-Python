from load_image import ft_load

def main():
    print("\033[1;94mFile that doesn't exist: ")
    ft_load("test")
    print()
    print("\033[1;94mFile that is not an image: ")
    ft_load("tester.py")
    print()
    print(ft_load("animal.jpeg"))


if __name__ == "__main__":
    main()