# Basic String Operations in Python

# Defining a String
str1 = "Hello, Python!"   # Using double quotes
str2 = 'Welcome to Strings'  # Using single quotes

# Multi-line String (Using Triple Quotes)
multi_line_str = """This is a
multi-line string example."""

# Printing Strings
print(str1)
print(str2)
print(multi_line_str)

# String Concatenation (Joining Strings)
greeting = "Hello" + " " + "World!"
print("Concatenated String:", greeting)

# String Repetition
repeat_str = "Python! " * 3
print("Repeated String:", repeat_str)

# Accessing Characters (Indexing)
print("First character of str1:", str1[0])   # H
print("Last character of str2:", str2[-1])  # s (negative indexing)

# Slicing a String (Substring)
print("Substring from str1 (index 0-5):", str1[0:5])  # Hello
print("Substring from str2 (from index 3 to end):", str2[3:])  # come to Strings

# String Length
print("Length of str1:", len(str1))

# Converting Case
print("Uppercase:", str1.upper())
print("Lowercase:", str2.lower())

# Replacing Part of a String
print("Replaced String:", str1.replace("Python", "World"))

# Checking Substring Presence
print("Does 'Python' exist in str1?", "Python" in str1)

# Splitting a String into a List
words = str2.split()  # Splits based on spaces
print("Splitted Words:", words)

# Joining a List of Words into a String
joined_str = " ".join(words)
print("Joined String:", joined_str)

