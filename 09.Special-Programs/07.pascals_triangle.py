from math import factorial

n = int(input("Enter the number of rows: "))

for i in range(n):
    print(" " * (n - i), end="")
    for j in range(i + 1):
        print(factorial(i) // (factorial(j) * factorial(i - j)), end=" ")
    print()

