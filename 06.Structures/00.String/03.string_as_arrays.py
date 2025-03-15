"""
Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.

However, Python does not have a character data type, a single character is simply a string with a length of 1.

Square brackets can be used to access elements of the string.
"""
a = "Hello, World!"
print(a[1]) #Get the character at position 1 (remember that the first character has the position 0)

"""
Looping Through a String
Since strings are arrays, we can loop through the characters in a string, with a for loop.
"""
for x in "banana": #Loop through the letters in the word "banana":
  print(x)
