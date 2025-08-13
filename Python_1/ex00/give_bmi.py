import numpy as np


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """Give a list of bmi with a list of height and a list of weight"""
    ERR_ARG1 = "I need 2 lists as argument"
    ERR_ARG2 = "I need only float and int in my lists"
    assert isinstance(height, list) and isinstance(weight, list), ERR_ARG1
    assert all(isinstance(x, (int, float)) for x in height) and\
        all(isinstance(y, (int, float)) for y in weight), ERR_ARG2
    assert len(height) == len(weight), "Lists have to have the same size"
    array_H = np.asarray(height)
    array_W = np.asarray(weight)
    bmi = array_W / (array_H * array_H)
    return bmi.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """apply_limit is a function taking a list of BMIs and returning a list of
Boolean"""
    ERR_ARG = "I need only float and int in bmi"
    assert isinstance(bmi, list) and isinstance(limit, int), "Wrong arguments"
    assert all(isinstance(x, (int, float)) for x in bmi), ERR_ARG
    array_bmi = np.asarray(bmi)
    limit_applied = array_bmi > limit
    return limit_applied.tolist()

# from give_bmi import give_bmi, apply_limit
# import sys


# def main():
#     weight = [165.3, 38.4]
#     try:
#         print("\033[1;94mLet's check with an arg that is not a list:")
#         print("\033[1;37mArgs of bmi: 23 | [165.3, 38.4]")
#         give_bmi(23, weight)
#     except AssertionError as e:
#         print(f"\033[1;91mAssertionError: {e}")
#     print()
#     try:
#         print("\033[1;94mLet's check with differents sized lists")
#         height = [2.71, 1.15, 3]
#         print(f"\033[1;37mLen of args: {len(height)} | {len(weight)}")
#         give_bmi(height, weight)
#     except AssertionError as e:
#         print(f"\033[1;91mAssertionError: {e}")
#     print()
#     try:
#         print("\033[1;94mLet's check with one wrong element of height")
#         height = [2.71, 1.15, "Not a float"]
#         print(f"\033[1;37mHeight: {height}")
#         give_bmi(height, weight)
#     except AssertionError as e:
#         print(f"\033[1;91mAssertionError: {e}")
#     print()
#     height = [2.71, 1.15]
#     print("\033[1;94mWith the height and weight of the subject:\033[1;92m")
#     bmi = give_bmi(height, weight)
#     print(bmi, type(bmi))
#     print(apply_limit(bmi, 26))


# if __name__ == "__main__":
#     main()
