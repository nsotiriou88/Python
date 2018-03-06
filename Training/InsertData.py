import sqlite3
import json


filenames = ['SomeFile']
db = sqlite3.connect("BasketExp.sqlite")
db.execute("PRAGMA journal_mode=WAL")
cursor = db.cursor()

for item in filenames:
    db.execute("CREATE TABLE IF NOT EXISTS " + item + " (timestamp REAL, id TEXT, meas TEXT, PRIMARY KEY(timestamp, id))")
    
    with open(item+'.txt') as file:
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

        data = json.loads(packet)
        strjson = str(data["meas"])

        try:
            # print((data["timestamp"], data["id"], strjson))
            cursor.execute("INSERT INTO " + item + " (timestamp, id, meas) VALUES (?, ?, ?)", (data["timestamp"], data["id"], strjson))
            db.commit()
        except KeyError:
            continue
        except sqlite3.IntegrityError:
            continue

