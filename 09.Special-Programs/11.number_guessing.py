import random

target = random.randint(1, 10)

while(1):
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == target:
        print("Congratulations! You guessed correctly.")
        break
    else:
        print(f"Wrong guess.")
