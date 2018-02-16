number = "9,223,372,036,854,775,807"
for i in range(0, len(number)):
    print(number[i])

# Same but notice the end command used in print
number = "9,223,372,036,854,775,807"
# for char in number:  ====> it will be the same. Extracts each character every time
for i in range(0, len(number)):
    # We would use: if char in '0123456789'
    if number[i] in '0123456789':
        print(number[i], end=' ') # can use \n,\t,\'anything'.

# Concatenating
number = "9,223,372,036,854,775,807"
cleanedNumber = ''

for i in range(0, len(number)):
    if number[i] in '0123456789':
        cleanedNumber = cleanedNumber + number[i]

newNumber = int(cleanedNumber)

print("\nThe number is {} ".format(newNumber))

# For with going in an [array of strings]
for state in ["not pinin'","no more", "a stiff", "bereft of life"]:
    print("This parrot is "+ state)
    # print("This parrot is {}".format(state))

# For within for loop and different stepping
for i in range(0, 30, 5):
    print("i is {} ".format(i))

for i in range(1,5):
    for j in range(1,5):
        print("{1} times {0} is {2}".format(i, j, i*j), end='\t')
        # If we exclude the end, it will print them vertical and not horizontal
    print("\n================")

# Breaking in loops
shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
    for item in shopping_list:
        if item == 'spam':
            break # If we use 'continue' instead, it will not continue
            # with the next line in the loop, but it doesn't break and
            # it will jump to the next item, eg. bread in our case.
        print("Buy " + item)

