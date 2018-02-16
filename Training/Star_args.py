def build_tuple(*args):
    return args

message_tuple = build_tuple("hello", "planet", "earth", "take", "me", "to", "your", "leader")
print(type(message_tuple))
print(message_tuple)

number_tuple = build_tuple(1, 2, 3, 4, 5, 6)
print(type(number_tuple))
print(number_tuple)

print()
#####################

def average(*args):
    print(type(args))
    print("args is {}:".format(args))
    print("*args is:", *args)  # This prints the Tuple without the parenthesis.
    
    mean = 0
    for arg in args:
        mean += arg
    return mean / len(args)

print(average(1, 2, 3, 4))
