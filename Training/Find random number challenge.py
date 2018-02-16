import random

highest = 1000
answer = random.randint(1, highest)

print("Please guess a number between 1 and {}: ".format(highest))
guess = 0   # initialize to any number outside of the valid range
while guess != answer:
    guess = int(input())
    if guess == 0:
        break
    if guess < answer:
        print("Please guess higher")
    elif guess > answer:  # guess must be greater than number
        print("Please guess lower")
    else:
        print("Well done, you guessed it")

