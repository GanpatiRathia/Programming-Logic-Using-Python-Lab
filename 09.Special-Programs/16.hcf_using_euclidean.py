def euclidean_hcf(a, b):
    while b:
        a, b = b, a % b
    return a

a, b = map(int, input("Enter two numbers: ").split())
print(f"HCF of {a} and {b} is {euclidean_hcf(a, b)}.")
