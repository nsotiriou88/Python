my_list = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

my_iterator = iter(my_list)
# This creates an iterator for an iterable object and points at the memory location

for i in range(0, len(my_list)):
    next_item = next(my_iterator)
    print(next_item)

print("#######################")
for i in my_list:
    print(i)

print('=' * 40)
#####################################

my_string = "abcdefghijklmnopqrstuvwxyz"
print(my_string.index('e'))
print(my_string[4])

print('=' * 40)
############################

decimals = range(0, 100)
print(decimals)

my_range = decimals[3:40:3]
print(my_range)

for i in my_range:
    print(i)

print('=' * 40)

for i in range(3, 40, 3):
    print(i)

print(my_range == range(3, 40, 3))

print('=' * 40)
############################

o = range(0, 100, 4)
print(o)
p = o[::5] # Here you are multiplying the range steps!!!
print(p)
for i in p:
    print(i)

print('=' * 40)
############################

a, b = 12, 13
print(a, b)

a, b = b, a # Multiple assignments at once
print("a is {}".format(a))
print("b is {}".format(b))

# Making a tuple
k=("Alpha", 5) # Better to use parenthesis, although in some cases they can be ignored
# Extracting/unpacking the values out from the tuple
k1,k2=k
print(k1)
print(k2)
