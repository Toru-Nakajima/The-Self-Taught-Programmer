def str_to_float():
    """
    Retuns float from string.
    :param x: float.
    :input: x.
    :print: float(x).
    """
    try:
        x = input("type a number:")
        x = float(x)
        print(x)
    except(ValueError):
        print("Invalid input.")

str_to_float()

