def ft_filter(function, iterable):
    """filter(function or None, iterable) --> filter object\
    \n\n\
Return an iterator yielding those items of iterable for which function(item)\n\
is true. If function is None, return the items that are true."""
    if function is None:
        function = bool

    for item in iterable:
        if function(item):
            yield item

# def is_pair(nb):
#     """Is number pair?"""
#     return nb % 2

# def main():
#     nombres = [1, 2, 3, 4, 5, 6]
#     resultat = ft_filter(is_pair, nombres)
#     res2 = filter(is_pair, nombres)
#     print(ft_filter.__doc__)
#     print(filter.__doc__)
#     print("\n")
#     print(list(resultat), " | ", list(res2))


# if __name__ == "__main__":
#     main()
