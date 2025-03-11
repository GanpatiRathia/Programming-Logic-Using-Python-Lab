count = 1
print("Before while loop: count =", count)

while count <= 5:
    print(count)
    if count == 3:
        print("Breaking the loop")
        break  # Exits the loop early
    count += 1
else:
    print("Loop ended as condition became False.")  # Skipped due to `break`

print("After while loop: count =", count)
