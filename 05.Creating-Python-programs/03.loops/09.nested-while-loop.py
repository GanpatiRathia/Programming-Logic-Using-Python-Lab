i = 1
print("Before nested loop")

while i <= 3:  # Outer loop
    j = 1
    while j <= 3:  # Inner loop
        print(f"i={i}, j={j}")
        j += 1
    i += 1

print("After nested loop")
