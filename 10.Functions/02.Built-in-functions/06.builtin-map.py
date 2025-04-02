"""
The map() function:
- Applies a given function to each item in an iterable.
- Returns an iterator (needs to be converted to list if required).
"""

def square_numbers():
    """Squares each number in a list using map()"""
    numbers = [1, 2, 3, 4, 5]
    squared = map(lambda x: x ** 2, numbers)
    print(list(squared))

def convert_to_uppercase():
    """Converts all strings in a list to uppercase using map()"""
    words = ["apple", "banana", "cherry"]
    upper_words = map(str.upper, words)
    print(list(upper_words))

def double_numbers():
    """Doubles each number in a list using map()"""
    numbers = [2, 5, 7, 10]
    doubled = map(lambda x: x * 2, numbers)
    print(list(doubled))

def add_lists():
    """Adds corresponding elements of two lists using map()"""
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    summed = map(lambda x, y: x + y, list1, list2)
    print(list(summed))

def calculate_lengths():
    """Calculates the length of each word in a list using map()"""
    words = ["hello", "world", "Python"]
    lengths = map(len, words)
    print(list(lengths))

def fahrenheit_to_celsius():
    """Converts a list of Fahrenheit temperatures to Celsius using map()"""
    fahrenheit = [32, 68, 100, 212]
    celsius = map(lambda f: (f - 32) * 5/9, fahrenheit)
    print(list(celsius))

def map_students_grades():
    """Converts numerical grades to letter grades using map()"""
    grades = [85, 72, 90, 60, 45]

    def grade_converter(score):
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        else:
            return "F"

    letter_grades = map(grade_converter, grades)
    print(list(letter_grades))

def square_numbers_list_comprehension():
    """Squares numbers using list comprehension"""
    numbers = [1, 2, 3, 4, 5]
    squared = [x ** 2 for x in numbers]
    print(squared)

def double_numbers_list_comprehension():
    """Doubles numbers using list comprehension"""
    numbers = [2, 5, 7, 10]
    doubled = [x * 2 for x in numbers]
    print(doubled)

# Main function with match-case
def main():
    print("Choose an option:")
    print("1. Square numbers using map()")
    print("2. Convert strings to uppercase using map()")
    print("3. Double numbers using map()")
    print("4. Add two lists element-wise using map()")
    print("5. Calculate word lengths using map()")
    print("6. Convert Fahrenheit to Celsius using map()")
    print("7. Convert numerical grades to letter grades using map()")
    print("8. Square numbers using list comprehension")
    print("9. Double numbers using list comprehension")

    choice = input("Enter your choice: ")
    match choice:
        case "1":
            square_numbers()
        case "2":
            convert_to_uppercase()
        case "3":
            double_numbers()
        case "4":
            add_lists()
        case "5":
            calculate_lengths()
        case "6":
            fahrenheit_to_celsius()
        case "7":
            map_students_grades()
        case "8":
            square_numbers_list_comprehension()
        case "9":
            double_numbers_list_comprehension()
        case _:
            print("Invalid choice, please select a valid option.")

# Run the main function
if __name__ == "__main__":
    main()

