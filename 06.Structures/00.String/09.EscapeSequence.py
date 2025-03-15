
try:
    txt = "We are the so-called "Vikings" from the north."
    print(txt)
except SyntaxError:
    print("Intentionally triggered SyntaxError")
except:
    print("Other error")

print("Continuing after the try/except")

txt = "We are the so-called \"Vikings\" from the north."
print(txt)
"""
Escape Characters
Other escape characters used in Python:

Code	Result	Try it
\'	Single Quote	
\\	Backslash	
\n	New Line	
\r	Carriage Return	
\t	Tab	
\b	Backspace	
\f	Form Feed	
\ooo	Octal value	
\xhh	Hex value

"""
