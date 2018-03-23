import sqlite3


# Connect to appropriate Database
database = "ThursdayExp"
db = sqlite3.connect(database+".sqlite")
cursor = db.cursor()
conn = sqlite3.connect(database+"_Converted.sqlite")
cursor2 = conn.cursor()

# Get all tables and remove bad characters
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
dbTables = cursor.fetchall()

tables = []

for table in dbTables:
    temp = list(table)
    tables.append(temp[0])

print('The tables in the Database are:', tables)

for table in tables:
    print("\n\tCompiling table:", table)
    conn.execute("CREATE TABLE " + table + " (timestamp REAL, id TEXT, meas TEXT, PRIMARY KEY(timestamp, id, meas))")
    cursor.execute("SELECT timestamp, id, meas FROM " + table)
    rows = cursor.fetchall()
    for row in rows:
        # print(row[2]) #DEBUG
        temp = ''
        i = 1
        for char in row[2]:
            if char == '{':
                temp += "{'anchor': '"
                i = 1
            elif char == ' ' and i == 1:
                temp += "', 'dist': "
                i += 1
            elif char == ' ' and i == 2:
                temp += ", 'tqf': "
                i += 1
            elif char == ' ' and i == 3:
                temp += ", 'toa': "
                i += 1
            elif char == ' ' and i == 4:
                temp += ", 'rssi': "
                i += 1
            elif char == ' ' and i == 5:
                temp += ", 'tqf2': "
                i += 1
            elif char == ' ' and i == 6:
                temp += ", 'rssi2': "
                i += 1
            elif char == '}':
                temp += "},"
            elif char == ']':
                temp = temp[:-1]
                temp += "]"
            else:
                temp += char


        cursor2.execute("INSERT INTO " + table + " (timestamp, id, meas) VALUES (?, ?, ?)", (row[0], row[1], temp))
        conn.commit()

        # print(temp) #DEBUG




#DEBUG

db.close()
conn.close()

print("Done!!!")
