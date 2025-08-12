import sys
from ft_filter import ft_filter


def make_lambda(size: int):
    """Return a lambda that check size of the arg"""
    return lambda word: len(word) > size


def main(av):
    ERR_ARG1 = "I need letters, digits or spaces only in my first arg"
    try:
        assert len(av) == 3, "I need 2 arguments"
        for c in av[1]:
            assert c.isalnum() or c == ' ', ERR_ARG1
        for c in av[2]:
            assert c.isdigit(), "I need only digits in my second arg."
    except AssertionError as e:
        print(f"AssertionError: {e}")
        exit(2)
    words = av[1].split()
    checklength = make_lambda(int(av[2]))
    print(f"{list(ft_filter(checklength, words))}")


if __name__ == "__main__":
    main(sys.argv)
