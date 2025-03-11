n = int(input("Enter the number of rows: "))

# Upper half of the pyramid
for i in range(1, n + 1):
    print("* " * i)

# Lower half of the pyramid
for i in range(n - 1, 0, -1):
    print("* " * i)

