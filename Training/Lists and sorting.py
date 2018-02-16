ipAddress = input("Please enter an IP address: ")
print(ipAddress.count("."))


parrot_list = ["non pinin'", "no more", "a stiff", "bereft of live"]

parrot_list.append("A Norwegian Blue") # Way of appending things in Python

for state in parrot_list:
    print("This parrot is " + state)


even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = even + odd
numbers_in_order = sorted(numbers)
# numbers.sorted()  ===> this will sort the numbers in the same variable
# but you cannot use it directly in print as a function, because it doesn't
# create a new variable...

print(numbers_in_order)

if numbers == numbers_in_order:
    print("The lists are equal")
else:
    print("The lists are not equal")
# Notice that it says not equal, although they have the same items, but one
# is not sorted.

if numbers_in_order == sorted(numbers):
    print("The lists are equal")
else:
    print("The lists are not equal")
print()
#################################

list_1 = []
list_2 = list()

print("List 1: {}".format(list_1))
print("List 2: {}".format(list_2))

if list_1 == list_2:
    print("The lists are equal")

print(list("The lists are equal"))
# Creates a list with each individual character in it

print()
print("@@@@@@@@@@@@@")
print()
even = [2, 4, 6, 8]

another_even = sorted(even, reverse=True)

print(another_even == even)

another_even.sort(reverse=True) # Reverse sorting with this
print(even)
# Although we updated another_even, it is passed to the even too.
# Both are sorted; they refer to the same underlying list

print()
###################################

even2 = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = [even2, odd] # Lists within the list

for number_set in numbers:
    print(number_set)

    for value in number_set:
        print(value)

print()
################################

menu = []
menu.append(["egg", "spam", "bacon"])
menu.append(["egg", "sausage", "bacon"])
menu.append(["egg", "spam"])
menu.append(["egg", "bacon", "spam"])
menu.append(["egg", "bacon", "sausage", "spam"])
menu.append(["spam", "bacon", "sausage", "spam"])
menu.append(["spam", "egg", "spam", "spam", "bacon", "spam"])
menu.append(["spam", "egg", "sausage", "spam"])
menu.append(["potatoes", "egg", "sausage", "kakaota"])

for meal in menu:
    if not "spam" in meal:
        print(meal)
        for ingredient in meal:
            print(ingredient)

