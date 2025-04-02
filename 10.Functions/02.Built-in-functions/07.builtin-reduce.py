"""
The reduce() function:
- Applies a given function cumulatively to the items of an iterable.
- Returns a single accumulated result.
- Available in the functools module.
"""

from functools import reduce  # Importing reduce from functools

def sum_numbers():
    """Calculates the sum of a list using reduce()"""
    numbers = [1, 2, 3, 4, 5]
    result = reduce(lambda x, y: x + y, numbers)  # x + y adds elements cumulatively
    print("Sum of numbers:", result)

def product_numbers():
    """Calculates the product of a list using reduce()"""
    numbers = [1, 2, 3, 4, 5]
    result = reduce(lambda x, y: x * y, numbers)  # x * y multiplies elements cumulatively
    print("Product of numbers:", result)

def find_maximum():
    """Finds the maximum value in a list using reduce()"""
    numbers = [12, 45, 2, 89, 30]
    result = reduce(lambda x, y: x if x > y else y, numbers)  # Returns the max element
    print("Maximum number:", result)

def find_minimum():
    """Finds the minimum value in a list using reduce()"""
    numbers = [12, 45, 2, 89, 30]
    result = reduce(lambda x, y: x if x < y else y, numbers)  # Returns the min element
    print("Minimum number:", result)

def concatenate_strings():
    """Concatenates a list of strings using reduce()"""
    words = ["Hello", " ", "World", "!", " ", "Python", " ", "is", " ", "awesome!"]
    result = reduce(lambda x, y: x + y, words)  # Joins strings together
    print("Concatenated string:", result)

def factorial():
    """Calculates the factorial of a number using reduce()"""
    n = 5  # Change this number to calculate factorial for a different value
    result = reduce(lambda x, y: x * y, range(1, n + 1))  # Multiplication from 1 to n
    print(f"Factorial of {n}:", result)

def sum_numbers_list_comprehension():
    """Calculates sum using list comprehension"""
    numbers = [1, 2, 3, 4, 5]
    result = sum([x for x in numbers])  # Alternative using sum()
    print("Sum using list comprehension:", result)

def product_numbers_list_comprehension():
    """Calculates product using list comprehension"""
    numbers = [1, 2, 3, 4, 5]
    result = 1
    for num in numbers:
        result *= num  # Alternative using loop
    print("Product using list comprehension:", result)

# Main function with match-case
def main():
    print("Choose an option:")
    print("1. Sum of numbers using reduce()")
    print("2. Product of numbers using reduce()")
    print("3. Find maximum value using reduce()")
    print("4. Find minimum value using reduce()")
    print("5. Concatenate strings using reduce()")
    print("6. Factorial of a number using reduce()")
    print("7. Sum of numbers using list comprehension")
    print("8. Product of numbers using list comprehension")

    choice = input("Enter your choice: ")
    match choice:
        case "1":
            sum_numbers()
        case "2":
            product_numbers()
        case "3":
            find_maximum()
        case "4":
            find_minimum()
        case "5":
            concatenate_strings()
        case "6":
            factorial()
        case "7":
            sum_numbers_list_comprehension()
        case "8":
            product_numbers_list_comprehension()
        case _:
            print("Invalid choice, please select a valid option.")

# Run the main function
if __name__ == "__main__":
    main()
