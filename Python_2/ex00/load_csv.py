import pandas as pd


def load(path: str) -> pd.DataFrame:
    """Load a csv file, prints format and return it as a pd.DataFrame"""
    ERR_ARG1 = " (parse error).\033[1;97m"
    ERR_ARG2 = "is not readable as text (encoding issue).\033[1;97m"
    try:
        db = pd.read_csv(path)
        print(f"Loading dataset of dimensions {db.shape}")
        return db
    except FileNotFoundError:
        print(f"\033[1;91mFile '{path}' is not findable.\033[1;97m")
    except PermissionError:
        print(f"\033[1;91mAccess denied: '{path}'.\033[1;97m")
    except pd.errors.EmptyDataError:
        print(f"\033[1;91mFile '{path}' is empty.\033[1;97m")
    except pd.errors.ParserError:
        print(f"\033[1;91mFile '{path}' is not a valid CSV" + ERR_ARG1)
    except UnicodeDecodeError:
        print(f"\033[1;91mFile '{path}'" + ERR_ARG2)
    except Exception as e:
        print(f"\033[1;91mErreur inattendue : {e}\033[1;97m")
    exit(1)

# from load_csv import load


# def main():
#     print("\033[1;94mFile that doesn't exist:")
#     load("test")
#     print()
#     print("\033[1;94mWrong format:")
#     load("bad.csv")
#     print()
#     print("\033[1;94mEmpty file:")
#     load("empty.txt")
#     print()
#     print("\033[1;94mGood attempt:\033[1;97m")
#     print(load("life_expectancy_years.csv"))
# # Add to_string for a complete visual, head or tail same use


# if __name__ == "__main__":
#     main()
