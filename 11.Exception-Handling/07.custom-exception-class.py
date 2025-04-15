class MyCustomError(Exception):
    pass

def risky_function():
    raise MyCustomError("Something went wrong!")

try:
    risky_function()
except MyCustomError as e:
    print("Caught custom exception:", e)
