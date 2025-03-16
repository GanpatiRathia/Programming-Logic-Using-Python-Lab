

# 1. Creating Lists
# Empty List
empty_list = []
print(f"Empty List: {empty_list}")

# List with initial values
my_list = [1, 2, 3, "hello", 4.5]
print(f"My List: {my_list}")

# List using range
numbers = list(range(5))  # Creates [0, 1, 2, 3, 4]
print(f"Numbers List: {numbers}")

# List from a string
letters = list("Python") # Creates ['P', 'y', 't', 'h', 'o', 'n']
print(f"Letters List: {letters}")

# 2. Accessing List Elements
print(f"First element of my_list: {my_list[0]}")
print(f"Last element of my_list: {my_list[-1]}")
print(f"Slice of my_list: {my_list[1:4]}") # elements at index 1,2,3

# 3. Modifying Lists
my_list[0] = 10  # Change the first element
print(f"Modified my_list: {my_list}")

my_list.append(6)  # Add an element to the end
print(f"Appended my_list: {my_list}")

my_list.insert(2, "inserted") # Insert at specific index.
print(f"Inserted my_list: {my_list}")

my_list.extend([7, 8, 9])  # Add multiple elements
print(f"Extended my_list: {my_list}")

del my_list[3]  # Remove element by index
print(f"Deleted my_list: {my_list}")

my_list.remove(4.5)  # Remove element by value
print(f"Removed my_list: {my_list}")

popped_element = my_list.pop() # removes and returns the last element.
print(f"Popped element: {popped_element}, my_list: {my_list}")

# 4. List Operations
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2  # Concatenation
print(f"Combined List: {combined_list}")

repeated_list = list1 * 3  # Repetition
print(f"Repeated List: {repeated_list}")

print(f"Length of my_list: {len(my_list)}")
print(f"Maximum of numbers: {max(numbers)}")
print(f"Minimum of numbers: {min(numbers)}")
print(f"Sum of numbers: {sum(numbers)}")

# 5. List Iteration
for item in my_list:
    print(item)

for index, item in enumerate(my_list):
    print(f"Index: {index}, Item: {item}")

# 6. List Comprehensions (Concise way to create lists)
squared_numbers = [x**2 for x in numbers]
print(f"Squared Numbers: {squared_numbers}")

even_numbers = [x for x in numbers if x % 2 == 0]
print(f"Even Numbers: {even_numbers}")

# 7. List Methods
my_list.reverse() # reverses the list in place.
print(f"Reversed list: {my_list}")

my_list.sort() # sorts the list in place. Only works if elements are comparable.
print(f"Sorted list: {my_list}")

my_list.clear() # removes all elements.
print(f"Cleared list: {my_list}")

# 8. Checking Membership
if "hello" in [1, 2, "hello"]:
  print("hello is in the list")

if 3 not in numbers:
  print("3 is not in the numbers list")

# 9. Copying Lists
original_list = [1, 2, 3]
copied_list = original_list[:] # Creates a shallow copy
print(f"Original list: {original_list}, Copied list: {copied_list}")

original_list[0] = 100
print(f"Original list after change: {original_list}, Copied list: {copied_list}") #copied list unchanged.
