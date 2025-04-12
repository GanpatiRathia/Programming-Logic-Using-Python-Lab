def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n - 1)

print(sum_n(5))  # Output: 15 (1+2+3+4+5)
