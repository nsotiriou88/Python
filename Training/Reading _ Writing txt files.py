jabber = open("/Users/Nicolas/Downloads/Python/Training/sample.txt", 'r')
# if you have it in your source file i/o, it only needs the name
# jabber = open("C:\\Documents and Settings\\tim\\My Documents\\sample.txt", 'r') ==> for windows
for line in jabber:
    if "jabberwock" in line.lower():
        print(line, end='')

jabber.close()  # Always remember to close the file. It may be corrupted otherwise.

print()
################################

# with open("/Users/Nicolas/Downloads/Python/Training/sample.txt", 'r') as jabber:  # No need to close the file!
#     for line in jabber:
#         if "JAB" in line.upper():
#             print(line, end='')
# Same, but doesn't need to close the file, since with takes care of it.
# In some cases, where error might occur, the file might remain open!

# with open("/Users/Nicolas/Downloads/Python/Training/sample.txt", 'r') as jabber:
#     line = jabber.readline()
#     while line:
#         print(line, end='')
#         line = jabber.readline()

with open("/Users/Nicolas/Downloads/Python/Training/sample.txt", 'r') as jabber:
    lines = jabber.readlines()
print(lines)

for line in lines:
    print(line, end='')  # removes the enter character in the end

print()
####################################
print()


# with open("sample.txt", 'r') as jabber:
#     lines = jabber.readlines()  # Reads the entire file
# print(lines)
#
# for line in lines[::-1]:
#     print(line, end='')
#
# with open("sample.txt", 'r') as jabber:
#     lines = jabber.read()
#
# for line in lines[::-1]:
#     print(line, end='')

# Method .read method is good for binary docs, rather than this occasion

###########################################
########   Writing on a file   ############
###########################################

# cities = ["Adelaide", "Alice Springs", "Darwin", "Melbourne", "Sydney"]
#
# with open("cities.txt", 'w') as city_file:
#     for city in cities:
#         print(city, file=city_file) # flush=True =>for writing directly, not buffer

# cities = []
#
# with open("cities.txt", 'r') as city_file:
#     for city in city_file:
#         cities.append(city.strip('\n')) # only strips from beginning or end of string
#
# print(cities)
# for city in cities:
#     print(city)

imelda = "More Mayhem", "Imelda MAy", "2011", (
    (1, "Pulling the Rug"), (2,"Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))

with open("imelda3.txt", 'w') as imelda_file:
    print(imelda, file=imelda_file)

with open("imelda3.txt", 'r') as imelda_file:
    contents = imelda_file.readline()

imelda = eval(contents)

print(imelda)
title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)


###########################################
########   Writing on a file   ############
###########################################


with open("sample.txt", 'a') as tables:
    for i in range(1, 11):
        for j in range(1, 11):
            print("{1:>2} times {0} is {2}".format(i, j, i * j), file=tables)
            # This is for printing towards right and reserving 2 spaces for
            # better syntax.
        print("-" * 20, file=tables)
