try:
    raise ValueError("Something bad happened")
except ValueError as e:
    print("Logging the error:", e)
    raise  # re-raises the same exception
