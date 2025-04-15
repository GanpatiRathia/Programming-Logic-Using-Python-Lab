def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Division by zero is not allowed"

print(divide(10, 2))
print(divide(10, 0))
