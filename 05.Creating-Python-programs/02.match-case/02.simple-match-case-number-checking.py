# Value before condition
num = 2
print("Before Match Statement: num =", num)

match num:
    case 1:
        print("Number is One")
    case 2:
        print("Number is Two")  # This block executes
    case 3:
        print("Number is Three")
    case _:
        print("Number is something else")  # Default case

print("After Match Statement: num =", num)
