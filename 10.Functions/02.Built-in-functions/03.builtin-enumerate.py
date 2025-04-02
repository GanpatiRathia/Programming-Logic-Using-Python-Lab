
# The enumerate() function in Python is used to add an index (counter) 
# to an iterable (like a list, tuple, or string) while iterating over

x = ('apple', 'banana', 'cherry')

for item in enumerate(x):  # Create a fresh iterator
    print(item)

for index, value in enumerate(x):  # Create a new iterator again
    print(str(index) + "\t" + value)
