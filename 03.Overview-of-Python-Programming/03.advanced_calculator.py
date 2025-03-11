import math

print("Advanced Python Calculator (No GUI, No Functions)")
print("Operations: +, -, *, /, %, ** (power), sqrt, log, sin, cos, tan, ! (factorial)")
print("Type 'exit' to quit.\n")

memory = 0  # Memory feature to store a value

while True:
    expr = input("Enter an expression: ").strip().lower()

    if expr == "exit":
        print("Exiting calculator.")
        break

    if expr == "mem":
        print(f"Memory: {memory}")
        continue

    if "sqrt" in expr:
        expr = expr.replace("sqrt", "math.sqrt")

    if "log" in expr:
        expr = expr.replace("log", "math.log")

    if "sin" in expr or "cos" in expr or "tan" in expr:
        expr = expr.replace("sin", "math.sin").replace("cos", "math.cos").replace("tan", "math.tan")

    if "!" in expr:
        num = int(expr.replace("!", ""))
        result = math.factorial(num)
    else:
        try:
            result = eval(expr)
        except Exception as e:
            print(f"Error: {e}")
            continue

    print(f"Result: {result}")
    memory = result  # Store last result in memory
