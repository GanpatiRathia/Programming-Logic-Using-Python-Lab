import random
import string

# 1 Roll a Dice Simulator
print(f"Rolling the dice... You got: {random.randint(1, 6)}")

# 2 Random Password Generator
length = int(input("\nEnter the length of the password: "))
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for _ in range(length))
print(f"Generated Password: {password}")

# 3 Random Lottery Number Picker
lottery_numbers = random.sample(range(1, 50), 6)  # Unique numbers from 1 to 49
print(f"\nLottery Numbers: {sorted(lottery_numbers)}")  # Sorted for better readability

# 4 Shuffle a List
items = input("\nEnter a list of items separated by spaces: ").split()
random.shuffle(items)
print(f"Shuffled List: {items}")

# 5 Random Selection from a List
names = input("\nEnter a list of names separated by spaces: ").split()
selected_name = random.choice(names)
print(f"Randomly Selected Name: {selected_name}")
