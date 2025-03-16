
# 1. Basic Function (No Arguments, No Return Value)
def greet():
    print("Hello, welcome to Python!\n")
print("1. Basic Function (No Arguments, No Return Value)")
greet()

# 2. Function with Parameters
def add_numbers(a, b):
    return a + b
print("2. Function with Parameters")
result = add_numbers(5, 10)
print("Sum: {} \n".format(result))

# 3. Function with Default Parameters
def greet_user(name="Guest"):
    print(f"Hello, {name}!\n")
print("3. Function with Default Parameters")
greet_user()          # Uses default value
greet_user("Alice")   # Uses provided argument

# 4. Function Returning Multiple Values
def arithmetic_operations(a, b):
    return a + b, a - b, a * b, a / b
print("4. Function Returning Multiple Values")
sum_, diff, prod, div = arithmetic_operations(10, 5)
print("Addition:", sum_)
print("Subtraction:", diff)
print("Multiplication:", prod)
print(f"Division: {div} \n")

print("Aliases for functions")
print(type(greet))  # <class 'function'>
print()
print(type(arithmetic_operations(1,2)))  # <class 'tuple'>
print()
greet_alias = greet
greet_alias()
greet_alias = greet()
greet_alias

# 5. Function with Variable Number of Arguments
def add_numbers(*args):
    return sum(args)
print("5. Function with Variable Number of Arguments")
print("Sum: {}\n".format(add_numbers(1, 2, 3, 4, 5)))

# 6. Function with Keyword Arguments
def greet_user(name, age):
    print(f"Hello, {name}! You are {age} years old.\n")   
print("6. Function with Keyword Arguments")
greet_user(name="Alice", age=25)
greet_user(age=25, name="Alice")

# 7. Function with Variable Number of Keyword Arguments
def greet_user(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}\n")
print("7. Function with Variable Number of Keyword Arguments")
greet_user(name="Alice", age=25, city="New York")

# 8. Function with Both Variable Number of Arguments and Keyword Arguments
def greet_user(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f"{key}: {value}\n")
print("8. Function with Both Variable Number of Arguments and Keyword Arguments")
greet_user("Hello", "World", name="Alice", age=25, city="New York")

# 9. Function with Docstring
def greet_user(name):
    """This function greets the user."""
    print(f"Hello, {name}!\n")
print("9. Function with Docstring")
print(greet_user.__doc__)

# 10. Function Annotations
def greet_user(name: str) -> None:
    print(f"\nHello, {name}!\n")
print("10. Function Annotations")
print(greet_user.__annotations__)

# 11. Lambda Functions
add_numbers = lambda a, b: a + b
print("\n11. Lambda Functions")
print(add_numbers(5, 10))

# 12. Recursive Function
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)
print("\n12. Recursive Function")
print("Factorial: {}\n".format(factorial(5)))

# 13. Nested Function
def outer_function():
    print("Outer function")
    
    def inner_function():
        print("Inner function\n")
        
    inner_function()
print("13. Nested Function")
outer_function()

# 14. Function as a Parameter
def greet():
    print("Hello!\n")

def welcome(greet):
    greet()
print("14. Function as a Parameter")
welcome(greet)

# 15. Function as a Return Value
def outer_function():
    print("Outer function")
    
    def inner_function():
        print("Inner function")
        
    return inner_function

print("15. Function as a Return Value")
inner = outer_function()
inner()

# 16. Function Closures
def outer_function(message):
    def inner_function():
        print(message)
        
    return inner_function

print("\n16. Function Closures")
greet = outer_function("Hello!")
greet()

# 17. Decorators
def decorator_function(func):
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
        
    return wrapper

def greet():
    print("Hello!")

print("\n17. Decorators")
greet = decorator_function(greet)
greet()

# 18. Decorator Syntax
def decorator_function(func):
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
        
    return wrapper

@decorator_function
def greet():
    print("Hello!")
print("\n18. Decorator Syntax")
greet()

# 19. Decorator with Arguments
def decorator_function(func):
    def wrapper(*args, **kwargs):
        print("Before function execution")
        func(*args, **kwargs)
        print("After function execution")
        
    return wrapper

@decorator_function
def greet(name):
    print(f"Hello, {name}!")
print("\n19. Decorator with Arguments")
greet("Alice")