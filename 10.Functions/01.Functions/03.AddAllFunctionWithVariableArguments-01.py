def add_all(*numbers):
    """
    Calculates the sum of an arbitrary number of numbers.

    Args:
        *numbers (int or float): Variable number of numbers.

    Returns:
        int or float: The sum of the numbers.
    """
    total = 0
    length = len(numbers)
    
    for i in range(length):
        total += numbers[i]
    return total

print(add_all(1, 2, 3))
print(add_all(10, 20, 30, 40))
