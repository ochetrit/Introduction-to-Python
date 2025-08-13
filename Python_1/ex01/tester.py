from array2D import slice_me

def main():
    try:
        print("\033[1;94mLet's check with family that is not a list:")
        print("\033[1;37mArgs of slice_me: 10 | 2 | 3")
        slice_me(10, 2, 3)
    except AssertionError as e:
        print(f"\033[1;91mAssertionError: {e}")
    print()
    family = [[1.80, 78.4],[2.15, 102.7],[2.10, 98.5],[1.88, 75.2]]
    try:
        print("\033[1;94mLet's check with start that is not an int")
        print(f"\033[1;37mArgs of slice_me: list | 'test' | 3")
        slice_me(family, "test", 3)
    except AssertionError as e:
        print(f"\033[1;91mAssertionError: {e}")
    print()
    try:
        print("\033[1;94mLet's check with one wrong element of family")
        print(f"\033[1;37mFamily[1]: 'salut'")
        family[1] = "salut"
        slice_me(family, 1 ,2)
    except AssertionError as e:
        print(f"\033[1;91mAssertionError: {e}")
    print()
    try:
        print("\033[1;94mLet's check with one wrong element of family")
        print(f"\033[1;37mFamily[1]: '[1]'")
        family[1] = [1]
        slice_me(family, 1 ,2)
    except AssertionError as e:
        print(f"\033[1;91mAssertionError: {e}")
    print()
    family[1] = [2.15, 102.7]
    print("\033[1;92mWith the test given by the subject:")
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))



# TESTER AVEC UNE MATRICE 1 1

if __name__ == "__main__":
    main()