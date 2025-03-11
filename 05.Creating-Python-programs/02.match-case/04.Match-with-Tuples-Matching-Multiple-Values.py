person = ("Alice", 25)
print("Before Match Statement: person =", person)

match person:
    case ("Alice", 25):
        print("Alice is 25 years old.")  # This block executes
    case ("Bob", 30):
        print("Bob is 30 years old.")
    case _:
        print("Unknown person.")

print("After Match Statement: person =", person)
