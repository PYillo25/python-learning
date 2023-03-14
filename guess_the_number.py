import random

num = random.randint(1, 10)
guess = None

while guess != num:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess < num:
        print("Too low")
    elif guess > num:
        print("Too high")
    else:
        print("You win!")
