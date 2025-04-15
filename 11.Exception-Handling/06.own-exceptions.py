def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    print("Age is valid")

try:
    check_age(-5)
except ValueError as e:
    print("Error:", e)
