def calculate_stats(numbers):
    """
    Calculates the sum and average of a list of numbers.

    Args:
        numbers (list): A list of numbers.

    Returns:
        tuple: A tuple containing the sum and average.
    """
    total = sum(numbers)
    average = total / len(numbers) if numbers else 0
    return total, average

result_sum, result_avg = calculate_stats([10, 20, 30])
print(f"Sum: {result_sum}, Average: {result_avg}").
