import sqlite3
import pytz
# import datetime


db = sqlite3.connect("accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)

for row in db.execute("SELECT * FROM history"):
    utc_time = row[0]
    local_time = pytz.utc.localize(utc_time).astimezone()
    print("{}\t{}".format(utc_time, local_time))
    print()
    print(row)
    # local_time = row[0]
    # print("{}\t{}".format(local_time, type(local_time)))
    # print(datetime.datetime.strptime(local_time, "%y-%m-%d %H:%M:%S"))

db.close()
