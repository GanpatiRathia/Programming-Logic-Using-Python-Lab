student = {"name": "John", "age": 20}
print("Before Match Statement: student =", student)

match student:
    case {"name": "John", "age": 20}:
        print("Student is John, 20 years old.")  # This block executes
    case {"name": "Alice", "age": 22}:
        print("Student is Alice, 22 years old.")
    case _:
        print("Unknown student.")

print("After Match Statement: student =", student)
