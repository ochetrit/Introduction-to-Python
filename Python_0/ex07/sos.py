import sys

NESTED_MORSE = {" ": "/",
                "A": ".-",
                "B": "-...",
                "C": "-.-.",
                "D": "-..",
                "E": ".",
                "F": "..-.",
                "G": "--.",
                "H": "....",
                "I": "..",
                "J": ".---",
                "K": "-.-",
                "L": ".-..",
                "M": "--",
                "N": "-.",
                "O": "---",
                "P": ".--.",
                "Q": "--.-",
                "R": ".-.",
                "S": "...",
                "T": "-",
                "U": "..-",
                "V": "...-",
                "W": ".--",
                "X": "-..-",
                "Y": "-.--",
                "Z": "--..",
                "1": ".----",
                "2": "..---",
                "3": "...--",
                "4": "....-",
                "5": ".....",
                "6": "-....",
                "7": "--...",
                "8": "---..",
                "9": "----.",
                "0": "-----"}


def encrypt(arg: str):
    """Return the sentence encoded"""
    encoded_words = []
    for c in arg:
        encoded_words.append(NESTED_MORSE[c.upper()])
    return " ".join(encoded_words)


def main(av):
    try:
        assert len(av) == 2, "I need 1 argument"
        for c in av[1]:
            assert c.isalnum() or c == ' ', "Only alnum characters or space"

        print(encrypt(av[1]))

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main(sys.argv)
