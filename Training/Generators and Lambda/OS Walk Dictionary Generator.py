import os


root = "music"

for path, directories, files in os.walk(root, topdown=True):  # os.walk is a generator => not loading everything at once.
    if files:
        print(path)
        first_split = os.path.split(path)
        print(first_split)
        second_split = os.path.split(first_split[0])
        print(second_split)
        for f in files:
            # song_details = f.strip('.emp3').split(' - ')
            song_details = f[:-5].split(' - ')
            print(song_details)
        print("*" * 40)
    # print(directories)
    # print(files)
    # input()

    # for f in files:
    #     print("\t{}".format(f))  # Linux do not print directory in alphabetical order.
