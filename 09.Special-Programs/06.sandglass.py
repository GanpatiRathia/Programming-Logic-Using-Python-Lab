n = int(input("Enter the number of rows: "))

# Upper half of sandglass
for i in range(n, 0, -1):
    print(" " * (n - i) + "* " * i)

# Lower half of sandglass
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)
