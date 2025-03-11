# Values before operation
a = 5  # 0b0101
b = 3  # 0b0011

print("Before Bitwise Operation: a =", a, ", b =", b)

# Bitwise operations
print("a & b (AND):", a & b)  # 0101 & 0011 = 0001 (1)
print("a | b (OR):", a | b)   # 0101 | 0011 = 0111 (7)
print("a ^ b (XOR):", a ^ b)  # 0101 ^ 0011 = 0110 (6)
print("~a (NOT):", ~a)        # NOT 0101 = -(5+1) = -6
print("a << 1 (Left Shift):", a << 1)  # 0101 << 1 = 1010 (10)
print("a >> 1 (Right Shift):", a >> 1)  # 0101 >> 1 = 0010 (2)

# Values remain unchanged after bitwise operations
print("After Bitwise Operation: a =", a, ", b =", b)
