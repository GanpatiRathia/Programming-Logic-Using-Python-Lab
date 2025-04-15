try:
    a = int("abc")
    b = 5 / 0
except (ValueError, ZeroDivisionError) as e:
    print("Caught an error:", e)
