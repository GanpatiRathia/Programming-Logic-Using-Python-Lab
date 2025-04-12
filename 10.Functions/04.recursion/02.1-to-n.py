def print_numbers(n):
    if n == 0:
        return
    print_numbers(n - 1)  # Recursively go down to 1
    print(n)              # Print on the way back

print_numbers(5)
