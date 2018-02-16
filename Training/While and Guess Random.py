available_exits = ["east", "north east", "south"]

chosen_exit = ""
while chosen_exit not in available_exits:
    chosen_exit = input("Please choose a direction: ")
    if chosen_exit == "quit":
        print("Game Over")
        break

else:
    print("aren't you glad you got out of there!")
# Check how the structure of the else is presented.
# It is mixed with the while, and it exits normally,
# it will go to else and print the message.

# Second part with random

import random

highest = 10
answer = random.randint(1, highest)

print("Please guess a number between 1 and {}: ".format(highest))
guess = int(input())
if guess != answer:
    if guess < answer:
        print("Please guess higher")
    else:  # guess must be greater than number
        print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it")
    else:
        print("Sorry, you have not guessed correctly")
else:
    print("You got it first time")

# Be aware that with only if statements, we have to implement
# infinate loops almost (up to the max number), in order to ensure
# that the user guesses right at some point. With the use of
# while, we can actually make it work with less code.