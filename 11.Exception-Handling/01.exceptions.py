\a =\
"""
What is Exception Handling?

Exception handling is a mechanism in Python used to gracefully manage runtime errors, without crashing the program.

Exception: An error that occurs during execution (e.g., dividing by zero, file not found, invalid input).

Handling: Catching and resolving the error using specific code so the program can continue running.
"""
print(a)

"""
Why Use Exception Handling?
Without it:
print(10 / 0)  # ZeroDivisionError, program crashes

With it:
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Can't divide by zero")
The goal is to make your programs robust, user-friendly, and error-resilient.
"""

"""
Basic Syntax
try:
    # Code that may raise an exception
except ErrorType:
    # Code that runs if the exception occurs
else:
    # Code that runs if no exception occurs (optional)
finally:
    # Code that always runs (optional)

"""

"""
Important Blocks
1. try
Used to wrap code that might throw an exception.
Python tries to execute the code.

2. except
Used to catch and handle specific exceptions.
You can handle multiple exceptions with multiple blocks or a tuple.

3. else
Runs only if the try block does not raise any exceptions.
Good for logic that should happen only when everything goes right.

4. finally
Runs no matter what, whether an error occurred or not.
Used for cleanup tasks (closing files, releasing resources, etc.)

"""

"""
Common Built-in Exceptions

Exception		Description
ZeroDivisionError	Division by zero
ValueError		Invalid value (e.g., int("abc"))
TypeError		Wrong data type operation
IndexError		Accessing list index out of range
KeyError		Accessing missing dictionary key
FileNotFoundError	File does not exist
ImportError		Module not found
"""

"""
#ZeroDivisionError
a = 5
b = 0
print(a / b)  # This will raise ZeroDivisionError
"""

"""
#ValueError - Invalid value
num = int("abc")  # Trying to convert a non-numeric string to int
"""

"""
#TypeError - Wrong data type operation
a = "5"
b = 3
print(a + b)  # Can't add string and integer
"""

"""
#IndexError – List index out of range
my_list = [1, 2, 3]
print(my_list[5])  # Index 5 does not exist
"""

"""
#KeyError – Accessing missing dictionary key
my_dict = {"name": "Alice"}
print(my_dict["age"])  # 'age' key is not in the dictionary
"""

"""
#FileNotFoundError – File does not exist
with open("non_existing_file.txt", "r") as f:
    content = f.read()
"""
"""
#ImportError – Module not found
import non_existing_module
"""

"""
Best Practices

Always catch specific exceptions (not generic Exception) unless absolutely necessary.
Use finally to clean up files, connections, etc.
Don't suppress exceptions silently unless there's a valid reason.
Log exceptions for debugging in real-world applications.
"""
