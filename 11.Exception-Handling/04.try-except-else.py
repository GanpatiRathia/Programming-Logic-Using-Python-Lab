try:
    num = int(input("Enter a positive number: "))
except ValueError:
    print("Not a number!")
else:
    print(f"You entered: {num}")
