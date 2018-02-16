import random
import math

test="Sarantapodarousa"
print(test[:10:2])
print(test[5:])

for i in range(1, 6):
    print ("No {:2} squared is {:3} and cubed is {:4}".format(i,i**2,i**3))
    # This way is better than using %s etc.
    # print("End") if you include the tab, it is going to print it in every loop.
print("End") # not printing in the loop, only once.
print()
name = input('please enter your name:\t') # We can use either "" or '' or mix of them.
age = int(input("How old are you {0}?:\t".format(name)))
# age = input("How old are you {0}?".format(name))
print("Your age is %d" %age) # Notice that this one does not need comma
# print("Your age is %s" %age) # Notice that this one does not need comma
print("Your name is", name, "\n") # ==> same results here; needs comma
print("ick" in name) # Tries to find if there is something similar in the string.
print()

# if Statement structure

if age > 23:
    print("You can go to the Casino!")
elif age == 23:
    print('You just made it!')
else:
    print("Please come back in {} years.".format(23-age))

if age>=23 and age<=27: # Better to use parenthesis to make it clear.
# we can use 22<age<27 or use not (age<22 or age>27)
# or use (age<22 or age>27) != True
    print('You enter for free!')

