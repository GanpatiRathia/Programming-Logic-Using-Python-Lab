x = 10
y = 10
z = [1, 2, 3]
w = [1, 2, 3]

print("Before Identity Operation: x =", x, ", y =", y, ", z =", z, ", w =", w)

# Identity operators
print("x is y:", x is y)    # True (same memory location)
print("z is w:", z is w)    # False (different objects)
print("z is not w:", z is not w)  # True

# Values remain unchanged after identity operations
print("After Identity Operation: x =", x, ", y =", y, ", z =", z, ", w =", w)
