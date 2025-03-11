# ===== ATOMS, IDENTIFIERS, AND KEYWORDS IN PYTHON =====

# ATOMS are the smallest elements of expressions in Python.
# Examples of atoms: Identifiers, Literals (numbers, strings), Tuples, Lists, Dictionaries, and Parenthesized expressions.

# Numeric literals (Atoms)
num = 42  # Integer literal
pi = 3.14  # Floating-point literal

# String literals (Atoms)
name = "Python"  # String literal

# Boolean literals (Atoms)
status = True  # Boolean literal (True, False)

# None (Atom)
nothing = None  # Represents the absence of a value

# Parenthesized expressions (Atoms)
expression = (2 + 3) * 5  # Parentheses group expressions

# Lists, Tuples, and Dictionaries (Atoms)
my_list = [1, 2, 3]  # List
my_tuple = (4, 5, 6)  # Tuple
my_dict = {"key": "value"}  # Dictionary

# IDENTIFIERS are names used to identify variables, functions, classes, etc.
# Rules for identifiers:
# 1. Can contain letters (A-Z, a-z), digits (0-9), and underscore (_)
# 2. Cannot start with a digit
# 3. Cannot be a Python keyword

_valid_variable = "Valid"
anotherValid123 = 100
# 123invalid = 50  # ❌ Invalid: Cannot start with a digit

# KEYWORDS are reserved words in Python that cannot be used as identifiers.
# Examples of Python keywords:
# False, None, True, and, as, assert, async, await, break, class, continue, def, del, elif, else, except, finally,
# for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield

# Using keywords correctly:
if status:  # 'if' is a keyword
    print("Status is True")

# def = 10  # ❌ Invalid: 'def' is a keyword and cannot be used as an identifier

# Checking all Python keywords
import keyword
print("Python Keywords:", keyword.kwlist)  # Prints all keywords in Python
