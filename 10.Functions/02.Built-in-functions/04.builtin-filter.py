"""
The filter() function:

Applies function to each item in iterable.

Keeps only True values (elements for which the function returns True).

Returns an iterator, which must be converted to a list if needed.
"""

def filter_adults():
    """Filters out adults (18+) from a list using filter()"""
    ages = [5, 12, 17, 18, 24, 32]
    
    def myFunc(x):
        return x >= 18  # Returns True if 18 or older
    
    adults = filter(myFunc, ages)
    print(list(adults))

def filter_adults_lambda():
    """Filters out adults using a lambda function"""
    ages = [5, 12, 17, 18, 24, 32]
    adults = filter(lambda x: x >= 18, ages)
    print(list(adults))

def filter_even_numbers():
    """Filters even numbers from a list"""
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_numbers = filter(lambda x: x % 2 == 0, numbers)
    print(list(even_numbers))

def filter_non_empty_strings():
    """Filters out empty and whitespace-only strings"""
    words = ["apple", "", "banana", " ", "cherry", "   ", "grape"]
    non_empty_words = filter(lambda word: word.strip() != "", words)
    print(list(non_empty_words))

def filter_prime_numbers():
    """Filters prime numbers from a range"""
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    numbers = range(1, 50)
    prime_numbers = filter(is_prime, numbers)
    print(list(prime_numbers))

def filter_students():
    """Filters students who passed (grade >= 50)"""
    students = [
        {"name": "Alice", "grade": 85},
        {"name": "Bob", "grade": 40},
        {"name": "Charlie", "grade": 75},
        {"name": "David", "grade": 90},
    ]

    passed_students = filter(lambda student: student["grade"] >= 50, students)
    print(list(passed_students))

def filter_adults_list_comprehension():
    """Filters adults using list comprehension"""
    ages = [5, 12, 17, 18, 24, 32]
    adults = [x for x in ages if x >= 18]
    print(adults)

def filter_even_numbers_list_comprehension():
    """Filters even numbers using list comprehension"""
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_numbers = [x for x in numbers if x % 2 == 0]
    print(even_numbers)

# Main function with match-case
def main():
    print("Choose an option:")
    print("1. Filter adults (filter function)")
    print("2. Filter adults (lambda function)")
    print("3. Filter even numbers")
    print("4. Filter non-empty strings")
    print("5. Filter prime numbers")
    print("6. Filter students who passed")
    print("7. Filter adults (list comprehension)")
    print("8. Filter even numbers (list comprehension)")
    
    choice = input("Enter your choice: ")

    match choice:
        case "1":
            filter_adults()
        case "2":
            filter_adults_lambda()
        case "3":
            filter_even_numbers()
        case "4":
            filter_non_empty_strings()
        case "5":
            filter_prime_numbers()
        case "6":
            filter_students()
        case "7":
            filter_adults_list_comprehension()
        case "8":
            filter_even_numbers_list_comprehension()
        case _:
            print("Invalid choice, please select a valid option.")

# Run the main function
if __name__ == "__main__":
    main()
