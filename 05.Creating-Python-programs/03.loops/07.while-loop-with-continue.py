num = 0
print("Before while loop: num =", num)

while num < 5:
    num += 1
    if num == 3:
        print("Skipping number", num)
        continue  # Skips the rest of the loop body
    print(num)

print("After while loop: num =", num)
