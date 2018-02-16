fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}
# if we add again a fruit with a key that already exists, it will not
# be a duplicate, but it will replace the value of the existing.
fruit2 = {"orange": "a sweet, orange, citrus fruit",
          "apple": "good for making cider",
          "lemon": "a sour, yellow citrus fruit",
          "grape": "a small, sweet fruit growing in bunches",
          "lime": "a sour, green citrus fruit"}

print(fruit)
print(fruit["lemon"])
fruit["pear"] = "an odd shaped apple"
print(fruit)
fruit["lime"] = "great with tequila"
print(fruit)
del fruit["lemon"]
fruit.clear() # Clears the table but keeps it, so there is no
# error if you print it, it's just empty
# del fruit ===> it will delete the entire dictionary!
print(fruit)
# print(fruit["tomato"]) ==> key error!

##########################
# ordered_keys = list(fruit.keys())
# ordered_keys.sort()

# ordered_keys = sorted(list(fruit.keys()))
# for f in ordered_keys:
#     print(f + " - " + fruit[f])

# for f in sorted(fruit.keys()): # ====> Fastest way of doing it!
# for f in fruit:
#     print(f  + " - " + fruit[f])
# for val in fruit.values(): # ====> Better to use keys instead of values
#     print(val)

print()

fruit_keys = fruit2.keys()
print(fruit_keys)
print(fruit2.values())

fruit2["tomato"] = "not nice with ice cream"
print(fruit_keys)
print(fruit2.values())
##########################
print()
for key in fruit2:
    print(key + " - " + fruit2[key])
while True:
    dict_key = input("Please enter a fruit: ")
    if dict_key == "quit":
        break
    if dict_key in fruit2:
        description = fruit2.get(dict_key) # .get function will not return
        # error, but the None message. We can also use default in get, without
        # using the if statement, like: fruit2.get(dict_key, "Not having" + dict_key)
        print(description)
    else:
        print("we don't have a " + dict_key)
# This while loop is infinite; it is like a waiting terminal for input
# There is no ordering in the Dictionaries; they are hash keys.
