n = int(input("Enter the number of terms: "))

a, b = 0, 1
for _ in range(n):
    if _ == n-1:
        print(a)
        break
    print(a, end=", ")
    a, b = b, a + b

