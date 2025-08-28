from give_bmi import give_bmi, apply_limit
import sys


def main():
    weight = [165.3, 38.4]
    try:
        print("\033[1;94mLet's check with an arg that is not a list:")
        print("\033[1;37mArgs of bmi: 23 | [165.3, 38.4]")
        give_bmi(23, weight)
    except AssertionError as e:
        print(f"\033[1;91mAssertionError: {e}")
    print()
    try:
        print("\033[1;94mLet's check with differents sized lists")
        height = [2.71, 1.15, 3]
        print(f"\033[1;37mLen of args: {len(height)} | {len(weight)}")
        give_bmi(height, weight)
    except AssertionError as e:
        print(f"\033[1;91mAssertionError: {e}")
    print()
    try:
        print("\033[1;94mLet's check with one wrong element of height")
        height = [2.71, 1.15, "Not a float"]
        print(f"\033[1;37mHeight: {height}")
        give_bmi(height, weight)
    except AssertionError as e:
        print(f"\033[1;91mAssertionError: {e}")
    print()
    height = [2.71, 1.15]
    print("\033[1;94mWith the height and weight of the subject:\033[1;92m")
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))




if __name__ == "__main__":
    main()