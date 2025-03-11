import math  # Importing the math module

# 1 Calculate Area of a Circle
radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius ** 2
print(f"Area of the circle with radius {radius}: {area:.4f}")

# 2 Find Square Root of a Number
num = float(input("\nEnter a number to find its square root: "))
sqrt_value = math.sqrt(num)
print(f"Square root of {num}: {sqrt_value:.4f}")

# 3 Calculate Factorial of a Number
num_factorial = int(input("\nEnter a number to find its factorial: "))
factorial_value = math.factorial(num_factorial)
print(f"Factorial of {num_factorial}: {factorial_value}")

# 4 Check if a Number is a Power of Two
num_power = int(input("\nEnter a number to check if it is a power of 2: "))
is_power_of_two = (math.log2(num_power)).is_integer()
print(f"Is {num_power} a power of 2? {is_power_of_two}")

# 5 Trigonometric Values Calculation
angle_deg = float(input("\nEnter an angle in degrees: "))
angle_rad = math.radians(angle_deg)  # Convert degrees to radians
sin_value = math.sin(angle_rad)
cos_value = math.cos(angle_rad)
tan_value = math.tan(angle_rad)
print(f"sin({angle_deg}°): {sin_value:.4f}")
print(f"cos({angle_deg}°): {cos_value:.4f}")
print(f"tan({angle_deg}°): {tan_value:.4f}")
