# area_of_circle.py
import math_utils  # Importing the math_utils module

# Take radius input from the user
radius = float(input("Enter the radius of the circle: "))

# Calculate area using PI from math_utils module
area = math_utils.PI * radius ** 2

# Display the result
print(f"The area of the circle with radius {radius} is: {area}")
