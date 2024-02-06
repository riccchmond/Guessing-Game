import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Hey, so I've thought of a number between 1 and {x}, can you guess: "))
        if guess > random_number:
            print("Oops,try again. That one is too high")
        elif guess < random_number:
            print("Oops,try again. That one is too low")

    print(f"Hazzah! You have guessed the number {random_number} correctly!")

guess(10)