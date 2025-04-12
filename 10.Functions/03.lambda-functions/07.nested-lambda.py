power = lambda x: lambda y: y ** x
square = power(2)
print(square(5))  # 25
