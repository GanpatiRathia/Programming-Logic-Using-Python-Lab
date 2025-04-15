try:
    x = int(input("Enter a number: "))
    try:
        result = 10 / x
    except ZeroDivisionError:
        print("Inner block: can't divide by zero.")
except ValueError:
    print("Outer block: not a valid number.")
