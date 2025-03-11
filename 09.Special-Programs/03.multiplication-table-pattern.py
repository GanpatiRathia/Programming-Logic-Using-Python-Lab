n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):  # Loop through rows
    for j in range(1, i + 1):  # Loop to print multiples
        print(i * j, end=" ")  # Multiply row index with column index
    print()  # Newline after each row
