# 1. Single Quote Problem:
try:
    txt = 'It\'s alright.'
    print(txt)
except SyntaxError:
    print("SyntaxError")
except:
    print("Other error")

print("Continuing after the try/except")

txt = 'It\'s alright.'
print(txt)

# 2. Backslash Problem:
try:
    txt = "This is a backslash: \\"
    print(txt)
except SyntaxError:
    print("SyntaxError")
except:
    print("Other error")

print("Continuing after the try/except")

txt = "This is a backslash: \\"
print(txt)

# 3. Newline Problem:
txt = "Hello\nWorld!"
print(txt)

# 4. Carriage Return Problem:
txt = "Hello\rWorld!"
print(txt)

# 5. Tab Problem:
txt = "Hello\tWorld!"
print(txt)

# 6. Backspace Problem:
txt = "Hello \bWorld!"
print(txt)

# 7. Form Feed Problem:
txt = "Hello\fWorld!"
print(txt)

# 8. Octal Value Problem:
txt = "\110\145\154\154\157"  # Hello
print(txt)

# 9. Hex Value Problem:
txt = "\x48\x65\x6c\x6c\x6f" # Hello
print(txt)

# 10. Double Quote Problem (already in the original code):
try:
    txt = "We are the so-called \"Vikings\" from the north."
    print(txt)
except SyntaxError:
    print("Intentionally triggered SyntaxError")
except:
    print("Other error")

print("Continuing after the try/except")

txt = "We are the so-called \"Vikings\" from the north."
print(txt)

#11. Mixing escape sequences
txt = "This is a tab:\t and a new line:\n and a backslash: \\"
print(txt)

#12. Escaping backslashes when they are used in windows paths.
txt = "C:\\Users\\MyUser\\Documents"
print(txt)

#13. using raw strings to avoid escaping backslashes.
txt = r"C:\Users\MyUser\Documents"
print(txt)

#14. Showing the effect of carriage return
txt = "Hello\rWorld"
print(txt)

#15. demonstrating form feed
txt = "Page1\fPage2"
print(txt)

#16. Using octal for non-printable characters.
txt = "Control Character (Bell):\007"
print(txt)

#17. Using hexadecimal for non-printable characters.
txt = "Control Character (Escape):\x1b"
print(txt)
