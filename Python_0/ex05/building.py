import sys
import string


def defarg(av):
    """Return the arg or use input to give an arg"""
    if len(av) == 1:
        arg = input("What is the text to count?\n")
        arg += "\n"
        return arg
    else:
        return av[1]


def main(av):
    try:
        assert len(av) <= 2, "More than one argument is provided"
        arg = defarg(av)
        print(f"The text contains {len(arg)} characters:")
        print(f"{sum(1 for c in arg if c.isupper())} upper letters")
        print(f"{sum(1 for c in arg if c.islower())} lower letters")
        nb_punct = sum(1 for c in arg if c in string.punctuation)
        print(f"{nb_punct} punctuation marks")
        print(f"{sum(1 for c in arg if c.isspace())} spaces")
        print(f"{sum(1 for c in arg if c.isdigit())} digits")
    except AssertionError as e:
        print(f'AssertionError: {e}')
        return 2
    except (EOFError, KeyboardInterrupt):
        print("No data provided to input function")
        return 1


if __name__ == "__main__":
    main(sys.argv)
