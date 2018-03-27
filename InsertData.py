import sqlite3
import json
from os import listdir


path = "/home/nicholas/Desktop/Friday/UWB"
# path = "/home/nicholas/Desktop/IMU from Manager/"
filenames = listdir(path)
print("List of files to compile for the database :", filenames, "\n")

db = sqlite3.connect("FridayExp_ALL.sqlite")
# db.execute("PRAGMA journal_mode=WAL")
cursor = db.cursor()

for item in filenames:
    db.execute("CREATE TABLE IF NOT EXISTS \"" + item + "\" (timestamp REAL, id TEXT, meas TEXT, PRIMARY KEY(timestamp, id, meas))")
    # db.execute("CREATE TABLE IF NOT EXISTS \"" + item + "\" (timestamp REAL, id TEXT, meas TEXT, acc TEXT, gyro TEXT, mag TEXT, PRIMARY KEY(timestamp, id, meas))")
    print("Registering", item, "to database...")

    with open(path+"/"+item) as file:
        content = file.readlines()

    # Strip out the newline character at the end of each line.
    content = [x.strip() for x in content]

    i = 0
    for packet in content:

        j = 0
        for char in packet:
            if char == "{":
                break

            j += 1

        packet = packet[j:len(packet)]
        content[i] = packet

        i += 1

        try:
            data = json.loads(packet)
        except json.decoder.JSONDecodeError:
            print("Check for weird line/character on line:", i, "at", item)
            continue

        strMeas = str(data["meas"])
        # strAcc = str(data["raw"]["acc"])
        # strGyro = str(data["raw"]["gyro"])
        # strMag = str(data["raw"]["mag"])

        try:
            cursor.execute("INSERT INTO \"" + item + "\" (timestamp, id, meas) VALUES (?, ?, ?)", (data["timestamp"], data["id"], strMeas))
            # cursor.execute("INSERT INTO \"" + item + "\" (timestamp, id, meas, acc, gyro, mag) VALUES (?, ?, ?, ?, ?, ?)", (data["timestamp"], data["id"], strMeas, strAcc, strGyro, strMag))
            db.commit()
        except KeyError:
            continue
        except sqlite3.IntegrityError:
            continue

db.close()

print("Done!!!")
