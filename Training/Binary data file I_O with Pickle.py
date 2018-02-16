import pickle   # for binary file like json and marshal (serialising data)


# with open("binary", 'bw') as bin_file:
#     bin_file.write(bytes(range(17)))
#
# with open("binary", 'br') as binFile:
#     for b in binFile:
#         print(b)

a = 65534       # FF FE
b = 65535       # FF FF
c = 65536       # 00 01 00 00
x = 2998302     # 02 2D C0 1E

with open("binary", 'bw') as bin_file:     # check the combination of b+w.
    bin_file.write(a.to_bytes(2, 'big'))
    bin_file.write(b.to_bytes(2, 'big'))
    bin_file.write(c.to_bytes(4, 'big'))
    bin_file.write(x.to_bytes(4, 'big'))    # starting from most significant digit
    bin_file.write(x.to_bytes(4, 'little')) # starting from least significant digit

with open("binary", 'br') as bin_file:
    e = int.from_bytes(bin_file.read(2), 'big')
    print(e)
    f = int.from_bytes(bin_file.read(2), 'big')
    print(f)
    g = int.from_bytes(bin_file.read(4), 'big')
    print(g)
    h = int.from_bytes(bin_file.read(4), 'big')
    print(h)
    i = int.from_bytes(bin_file.read(4), 'big') # by replacing big with little, we get
    # the right value for the number, although with big it is not the same because we
    # are reading the bytes in the opposite order that they are stored.
    print(i)

#######################################
print()
#         -----Pickling-----
print()
#######################################


imelda = ('More Mayhem',
          'IMelda May',
          '2011',
          ((1, 'Pulling the Rug'),
           (2, 'Psycho'),
           (3, 'Mayhem'),
           (4, 'Kentish Town Waltz')))

# with open("imelda.pickle", "wb") as pickle_file:
#     pickle.dump(imelda, pickle_file)


# with open("imelda.pickle", "rb") as imelda_pickled:
#     imelda2 = pickle.load(imelda_pickled)
#
# print(imelda2)
#
# album, artist, year, track_list = imelda2
#
# print(album)
# print(artist)
# print(year)
# for track in track_list:
#     track_number, track_title = track
#     print(track_number, track_title)

###################################
###################################

even = list(range(0, 10, 2))
odd = list(range(1, 10, 2))

with open("imelda.pickle", "wb") as pickle_file:
    pickle.dump(imelda, pickle_file, protocol=pickle.HIGHEST_PROTOCOL)
    pickle.dump(even, pickle_file, protocol=0)      # most human readable protocol
    pickle.dump(odd, pickle_file, protocol=pickle.DEFAULT_PROTOCOL)
    pickle.dump(2998302, pickle_file, protocol=pickle.DEFAULT_PROTOCOL)

with open("imelda.pickle", "rb") as imelda_pickled:
    imelda2 = pickle.load(imelda_pickled)
    even_list = pickle.load(imelda_pickled)
    odd_list = pickle.load(imelda_pickled)
    x = pickle.load(imelda_pickled)

print(imelda2)

album, artist, year, track_list = imelda2

print(album)
print(artist)
print(year)
for track in track_list:
    track_number, track_title = track
    print(track_number, track_title)

print('=' * 40)

for i in even_list:
    print(i)

print('=' * 40)

for i in odd_list:
    print(i)

print('=' * 40)

print(x)

print('=' * 40)


# Pickle stream to remove the data file!!!

pickle.loads(b"cos\nsystem\n(S'rm imelda.pickle'\ntR.")   # Mac/Linux
# pickle.loads(b"cos\nsystem\n(S'rm binary'\ntR.")   # Mac/Linux => use it for other files too!
# pickle.loads(b"cos\nsystem\n(S'del imelda.pickle'\ntR.")  # Windows
