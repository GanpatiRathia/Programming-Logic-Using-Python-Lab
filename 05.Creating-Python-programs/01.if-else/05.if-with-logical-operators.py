# Example: Checking if a number is in a range
num = 50
print("Before Condition: num =", num)

if num > 30 and num < 60:  # Both conditions must be True
    print("The number is in the range of 30-60.")

if num < 40 or num > 45:  # At least one condition must be True
    print("The number is either less than 40 or greater than 45.")

if not (num < 30):  # 'not' reverses the condition
    print("The number is not less than 30.")

print("After Condition: num =", num)
