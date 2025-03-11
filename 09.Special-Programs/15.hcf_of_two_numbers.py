a, b = map(int, input("Enter two numbers: ").split())

hcf = 1
for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        hcf = i

print(f"HCF of {a} and {b} is {hcf}.")
