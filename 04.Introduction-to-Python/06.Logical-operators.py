# Values before operation
p = True
q = False

print("Before Logical Operation: p =", p, ", q =", q)

# Logical operations
print("p and q:", p and q)  # False (Both must be True)
print("p or q:", p or q)    # True (At least one must be True)
print("not p:", not p)      # False (Negation)
print("not q:", not q)      # True

# Values remain unchanged after logical operations
print("After Logical Operation: p =", p, ", q =", q)
