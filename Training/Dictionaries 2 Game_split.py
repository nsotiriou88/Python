fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

print(fruit)
print(fruit.items())
f_tuple = tuple(fruit.items())
print(f_tuple)

for snack in f_tuple:
    item, description = snack
    print(item + " is " + description)

print(dict(f_tuple))

print()
############################
locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0} }

vocabulary = { "QUIT":  "Q",
               "NORTH": "N",
               "SOUTH": "S",
               "EAST":  "E",
               "WEST":  "W"}

# print(locations[0].split())
# print(locations[3].split("-"))
# print(' '.join(locations[0].split()))

loc = 1
while True:
    availableExits = ", ".join(exits[loc].keys())

    print(locations[loc])

    if loc == 0:
        break

    direction = input("Available exits are " + availableExits + " ").upper()
    print()
    # Parse the user input, using our vocabulary dictionary if necessary
    if len(direction) > 1:   # more than one letter, so check vocabulary
        words = direction.split()  # better this way, instead of iterating through
        # the dictionary for the key values matching.
        for word in words:   # Checking if it contains the word
            if word in vocabulary:  # without words: if word in vocabulary:
                direction = vocabulary[word]
                break

    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("You cannot go in that direction")


# Old program

###########################
#
# locations = {0: "You are sitting in front of a computer learning Python",
#              1: "You are standing at the end of a road before a small brick building",
#              2: "You are at the top of a hill",
#              3: "You are inside a building, a well house for a small stream",
#              4: "You are in a valley beside a stream",
#              5: "You are in the forest"}
#
# exits = [{"Q": 0},
#          {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
#          {"N": 5, "Q": 0},
#          {"W": 1, "Q": 0},
#          {"N": 1, "W": 2, "Q": 0},
#          {"W": 2, "S": 1, "Q": 0}]
# # List with dictionaries
#
# loc = 1
# while True:
#     availableExits = ", ".join(exits[loc].keys()) # Always starts a new string.
#     # Best way of concatenating a string, because it is efficient for sequences
#     # and no loop is required either!
#
#     print(locations[loc])
#
#     if loc == 0:
#         break
#
#     direction = input("Available exits are " + availableExits + " : ").upper()
#     print()
#     if direction in exits[loc]:
#         loc = exits[loc][direction]
#     else:
#         print("You cannot go in that direction")
