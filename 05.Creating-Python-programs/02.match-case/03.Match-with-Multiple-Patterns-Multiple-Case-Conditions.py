fruit = "apple"
print("Before Match Statement: fruit =", fruit)

match fruit:
    case "apple" | "mango" | "banana":
        print("It's a fruit.")  # This block executes
    case "carrot" | "potato":
        print("It's a vegetable.")
    case _:
        print("Unknown item.")

print("After Match Statement: fruit =", fruit)

