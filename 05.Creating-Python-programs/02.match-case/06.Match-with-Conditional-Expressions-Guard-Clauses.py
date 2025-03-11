number = 15
print("Before Match Statement: number =", number)

match number:
    case num if num % 2 == 0:
        print(f"{num} is even.")
    case num if num % 2 != 0:
        print(f"{num} is odd.")  # This block executes

print("After Match Statement: number =", number)
