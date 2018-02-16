import sqlite3

db = sqlite3.connect("contacts.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contacts(name, phone, email) VALUES('Tim', 6545678, 'tim@email.com')")
db.execute("INSERT INTO contacts VALUES('Brian', 1234, 'brian@myemail.com')")

cursor = db.cursor()  # help to iterate through the database without overfloading memory.
cursor.execute("SELECT * FROM contacts")

# print(cursor.fetchall())

print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())  # returns nothing, as we fetched all existing data; same for the next loop.

for name, phone, email in cursor:
# for name, phone, email in db.execute("SELECT * FROM contacts"):  # useful when we do NOT use cursor
    print(name)
    print(phone)
    print(email)
    print("-" * 20)

cursor.close()  # need to close cursor!
# db.commit()  # for making changes permanent.
db.close()  # need to close database!

##################################
# Second Part - Updating Entries #
##################################
db = sqlite3.connect("contacts.sqlite")

new_email = "anotherupdate@update.com"
# phone = "1234;drop table contacts"
phone = input("Please enter the phone! ")

# update_sql = "UPDATE contacts SET email = 'anotherupdate@update.com' WHERE phone = 1234"
# update_sql = "UPDATE contacts SET email = ? WHERE phone = ?" # Placeholders are safer as Python takes care about injections.
update_sql = "UPDATE contacts SET email = '{}' WHERE phone = {}".format(new_email, phone)
update_cursor = db.cursor()
# update_cursor.execute(update_sql, (new_email, phone))
update_cursor.execute(update_sql)
# update_cursor.executescript(update_sql) # Dangerous for injection Attacks. Will allow multiple statements to execute.
print("{} rows updated".format(update_cursor.rowcount))

print()
print("Are connections the same: {}".format(update_cursor.connection == db))
print()

update_cursor.connection.commit()
update_cursor.close()

for name, phone, email in db.execute("SELECT * FROM contacts"):
    print(name)
    print(phone)
    print(email)
    print("-" * 20)

db.close()

####### Printing Database Checking ########
conn = sqlite3.connect("contacts.sqlite")

input_name = input("Please enter a name to search for: ")

# for row in conn.execute("SELECT * FROM contacts WHERE name = ?", (input_name,)):
for row in conn.execute("SELECT * FROM contacts WHERE name LIKE ?", (input_name,)):
# for row in conn.execute("SELECT * FROM sqlite_master"):  # injecting code to find all tables in database.
    print(row)

conn.close()
