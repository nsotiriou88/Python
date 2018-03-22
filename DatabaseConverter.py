import sqlite3


# Connect to appropriate Database
db = sqlite3.connect("TESTING_NICK.sqlite")
cursor = db.cursor()

# Get all tables and remove bad characters
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
results = cursor.fetchall()
i = 0
for table in results:
    print(results[i])
    results[i] = table[2:-3]
    print(results[i])

    i += 1

#DEBUG
print(results)
print(type(results), len(results))
print(results[0])

print(results[0][:-3])
