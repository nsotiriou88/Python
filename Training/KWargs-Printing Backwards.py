# def print_backwards(*args, end=' ', **kwargs):  # Removes end Key Word from being included in kwargs.
def print_backwards(*args, **kwargs):
    print(kwargs)
    # kwargs.pop('end', None)  # Use this with pop to work together.
    for word in args[::-1]:
        print(word[::-1], **kwargs)
        # print(word[::-1], end=' ', **kwargs)  # Use this with pop to work together.

with open("backwards.txt", 'w') as backwards:
    print_backwards("hello", "planet", "earth", "take", "me", "to", "your", "leader", end=' ', file=backwards)
    print_backwards("hello", "planet", "earth", "take", "me", "to", "your", "leader", end=' ')

# ===================================

def print_backwards2(*args, **kwargs):
    end_character = kwargs.pop('end', '\n')
    sep_character = kwargs.pop('sep', ' ')
    for word in args[:0:-1]:    # change the range
        print(word[::-1], end=sep_character, **kwargs)
    print(args[0][::-1], end=end_character, **kwargs)      # and print the first word separately
    # print(end=end_character)  # which means we don't need this line


def backwards_print(*args, **kwargs):
    sep_character = kwargs.pop('sep', ' ')
    print(sep_character.join(word[::-1] for word in args[::-1]), **kwargs)

with open("backwards.txt", 'w') as backwards:
    print_backwards2("hello", "planet", "earth", "take", "me", "to", "your", "leader", end='\n')
    print("Another String")


print()
print("hello", "planet", "earth", "take", "me", "to", "your", "leader", end='', sep='\n**\n')
print_backwards2("hello", "planet", "earth", "take", "me", "to", "your", "leader", end='', sep='\n**\n')
print("=" * 10)
