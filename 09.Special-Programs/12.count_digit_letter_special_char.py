s = input("Enter a string: ")

digits = sum(c.isdigit() for c in s)
letters = sum(c.isalpha() for c in s)
special_chars = len(s) - digits - letters

print(f"Letters: {letters}, Digits: {digits}, Special Characters: {special_chars}")
