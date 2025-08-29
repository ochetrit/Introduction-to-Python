from load_csv import load


def main():
    print("\033[1;94mFile that doesn't exist:")
    load("test")
    print()
    print("\033[1;94mWrong format:")
    load("bad.csv")
    print()
    print("\033[1;94mEmpty file:")
    load("empty.txt")
    print()
    print("\033[1;94mGood attempt:\033[1;97m")
    print(load("life_expectancy_years.csv"))
# Add to_string for a complete visual, head or tail same use


if __name__ == "__main__":
    main()
