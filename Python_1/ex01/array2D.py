import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """Function that takes as parameters a 2D array, prints its shape,\
 and returns a truncated version of the array based on the provided\
 start and end arguments"""
    ERR_ARG = "Start and end have to be int"
    ERR_FAMILY = "Every element of the list has to be a list"
    ERR_FAMILY2 = "Each list of family should have the same size"
    assert isinstance(family, list), "First arg has to be a list"
    assert isinstance(start, int) and isinstance(end, int), ERR_ARG
    assert all(isinstance(x, list) for x in family), ERR_FAMILY
    if len(family) == 0:
        return None
    size = len(family[0])
    assert all(size == len(x) for x in family), ERR_FAMILY2
    print(f"\033[1;37mMy shape is : ({len(family)}, {size})")
    array_2D = np.asarray(family)
    array_sliced = array_2D[start: end, :]
    print(f"\033[1;37mMy new shape is : ({len(array_sliced)}, {size})")
    return array_sliced.tolist()


# from array2D import slice_me

# def main():
#     try:
#         print("\033[1;94mLet's check with family that is not a list:")
#         print("\033[1;37mArgs of slice_me: 10 | 2 | 3")
#         slice_me(10, 2, 3)
#     except AssertionError as e:
#         print(f"\033[1;91mAssertionError: {e}")
#     print()
#     family = [[1.80, 78.4],[2.15, 102.7],[2.10, 98.5],[1.88, 75.2]]
#     try:
#         print("\033[1;94mLet's check with start that is not an int")
#         print(f"\033[1;37mArgs of slice_me: list | 'test' | 3")
#         slice_me(family, "test", 3)
#     except AssertionError as e:
#         print(f"\033[1;91mAssertionError: {e}")
#     print()
#     try:
#         print("\033[1;94mLet's check with one wrong element of family")
#         print(f"\033[1;37mFamily[1]: 'salut'")
#         family[1] = "salut"
#         slice_me(family, 1 ,2)
#     except AssertionError as e:
#         print(f"\033[1;91mAssertionError: {e}")
#     print()
#     try:
#         print("\033[1;94mLet's check with one wrong element of family")
#         print(f"\033[1;37mFamily[1]: '[1]'")
#         family[1] = [1]
#         slice_me(family, 1 ,2)
#     except AssertionError as e:
#         print(f"\033[1;91mAssertionError: {e}")
#     print()
#     family[1] = [2.15, 102.7]
#     print("\033[1;92mWith the test given by the subject:")
#     print(slice_me(family, 0, 2))
#     print(slice_me(family, 1, -2))


# # TESTER AVEC UNE MATRICE 1 1

# if __name__ == "__main__":
#     main()
