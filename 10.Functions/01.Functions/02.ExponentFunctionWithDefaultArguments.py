def power(base, exponent=2):
    """
    Calculates the power of a base raised to an exponent.

    Args:
        base (int or float): The base number.
        exponent (int): The exponent (defaults to 2).

    Returns:
        int or float: The result of the calculation.
    """
    return base ** exponent

print(power(3))      # 3 squared (exponent=2)
print(power(2, 3))   # 2 cubed (exponent=3)
