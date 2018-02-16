import shelve
# Shelves are databases files and their purpose is to aid in the memory
# consumption. Less memory reserved. Values are pickled before stored.
# Shelve keys MUST BE strings!!!

# with shelve.open('ShelfTest') as fruit:   # if we want to safely exit
fruit = shelve.open('ShelfTest')
# we can also define fruit as a dictionary immediately!
fruit['orange'] = "a sweet, orange, citrus fruit"
fruit['apple'] = "good for making cider"
fruit['lemon'] = "a sour, yellow citrus fruit"
fruit['grape'] = "a small, sweet fruit growing in bunches"
fruit['lime'] = "a sour, green citrus fruit"

# print(fruit["lemon"])
# print(fruit["grape"])
####
# fruit["lime"] = "great with tequila"
#
# for snack in fruit:
#     print(snack + ": " + fruit[snack])

# Checking and printing the dictionary contains:

# while True:
#     dict_key = input("Please enter a fruit: ").lower()
#     if dict_key == "quit" or dict_key == "q":
#         break
#     # 2 ways to do it (get method):
#     # description = fruit.get(dict_key, 'Wrong entry: ' + dict_key)
#     # print(description)
#
#     if dict_key in fruit:
#         description = fruit[dict_key]
#         print(description)
#     else:
#         print("We don't have a " + dict_key)

# Ordering the random ordered keys in the dictionary:

# ordered_keys = list(fruit.keys())
# ordered_keys.sort()
#
# for f in ordered_keys:
#     print(f + " - " + fruit[f])

# Printing the values and the items in the database:
for v in fruit.values():
    print(v)

print(fruit.values())

for f in fruit.items():
    print(f)

print(fruit.items())


# print(fruit)    # not printing the entire dictionary entries!!!
fruit.close()   # needed if not using with to open file; manually close.

print(fruit)


##########################
print()
##########################


# with shelve.open("bike") as bike:
#     # bike["make"] = "Honda"
#     # bike["model"] = "250 dream"
#     # bike["colour"] = "red"
#     # bike["engine_size"] = 250
#
#     # del bike['engin_size']  # Deleting from the database
#
#     for key in bike:
#         print(key)
#
#     print('=' * 40)
#
#     print(bike["engine_size"])
#     # print(bike["engin_size"])
#     print(bike["colour"])

##############################
##########   IMPORTANT!!!  ###########
# Every time we run the program, if the database file exists, it
# will append the new entries and change the existing ones, rather
# than erasing the entire database and creating a whole new one
# from the beginning.

##############################
##############################


blt = ["bacon", "lettuce", "tomato", "bread"]
beans_on_toast = ["beans", "bread"]
scrambled_eggs = ["eggs", "butter", "milk"]
soup = ["tin of soup"]
pasta = ["pasta", "cheese"]

# with shelve.open('recipes') as recipes:
with shelve.open('recipes', writeback=True) as recipes: # for writing
# immediately, without using temp var.
    recipes["blt"] = blt
    recipes["beans on toast"] = beans_on_toast
    recipes["scrambled eggs"] = scrambled_eggs
    recipes["pasta" ] = pasta
    recipes["soup"] = soup

    # recipes["blt"].append("butter")
    # recipes["pasta"].append("tomato")

# The reason for using a temp var, is because of shelve's functionality
# that tries to minimise the disk usage and therefore this happens.

    # temp_list = recipes["blt"]
    # temp_list.append("butter")
    # recipes["blt"] = temp_list
    #
    # temp_list = recipes["pasta"]
    # temp_list.append("tomato")
    # recipes["pasta"] = temp_list

# works a lot with writeback set to True only
    recipes["soup"].append("croutons")

    # recipes["soup"] = soup
    # recipes.sync()    # forces the cache to unload, but also clears it.
    # soup.append("cream")

    for snack in recipes:
        print(snack, recipes[snack])
