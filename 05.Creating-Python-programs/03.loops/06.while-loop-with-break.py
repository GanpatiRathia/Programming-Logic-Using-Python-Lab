num = 1
print("Before while loop: num =", num)

while num < 10:
    if num == 5:
        print("Breaking loop at:", num)
        break  # Exits the loop
    print(num)
    num += 1

print("After while loop: num =", num)
