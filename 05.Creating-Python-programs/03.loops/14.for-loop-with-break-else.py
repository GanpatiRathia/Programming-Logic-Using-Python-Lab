print("Before for loop")

for i in range(5):
    print(i)
    if i == 2:
        print("Breaking the loop")
        break  # Exits the loop early
else:
    print("Loop completed successfully.")  # Skipped due to `break`

print("After for loop")
