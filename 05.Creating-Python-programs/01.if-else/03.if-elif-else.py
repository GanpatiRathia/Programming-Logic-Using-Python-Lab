# Example: Checking grades
marks = 85
print("Before Condition: marks =", marks)

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")  # This block executes
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: F")

print("After Condition: marks =", marks)
