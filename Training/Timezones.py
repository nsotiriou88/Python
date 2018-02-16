# The datetime module
import datetime

# print(datetime.datetime.today())
# print(datetime.datetime.now())
# print(datetime.datetime.utcnow())
# print()


# Time Module and different Timezones
import time

print("The epoch on this system starts at " + time.strftime('%c', time.gmtime(0)))

print("The current timezone is {0} with an offset of {1}".format(time.tzname[0], time.timezone))

if time.daylight !=0:
    print()
    print("\tDaylight Saving Time is in effect for this location")
    print("\tThe DST timezone is " + time.tzname[1])

print()
print("Local time is " + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
print("UTC time is " + time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()))


# The pytz module
# print()
# import pytz

# country = 'Europe/Moscow'

# tz_to_display = pytz.timezone(country)
# local_time = datetime.datetime.now(tz=tz_to_display)
# print("The time in {} is {}".format(country, local_time))
# print("UTC is {}".format(datetime.datetime.utcnow()))

# for x in pytz.all_timezones:
#     print(x)
#
# for x in sorted(pytz.country_names):
#     print(x + ": " + pytz.country_names[x])
#
# for x in sorted(pytz.country_names):
#     print("{}: {}".format(x, pytz.country_names[x]), end=': ')
#     if x in pytz.country_timezones:
#         for zone in sorted(pytz.country_timezones[x]):
#             tz_to_display = pytz.timezone(zone)
#             local_time = datetime.datetime.now(tz=tz_to_display)
#             print("\t\t{}: {}".format(zone, local_time))
#     else:
#         print("\t\tNo time zone defined")


# Program that is aware of time!!!
# print()
# local_time = datetime.datetime.now()
# utc_time = datetime.datetime.utcnow()

# print("Naive local time {}".format(local_time))
# print("Naive UTC {}".format(utc_time))

# aware_local_time = pytz.utc.localize(local_time).astimezone()
# aware_utc_time = pytz.utc.localize(utc_time)

# print("Aware local time{}, time zone {} ".format(aware_local_time, aware_local_time.tzinfo))
# print("Aware UTC {}, time zone {}".format(aware_utc_time, aware_utc_time.tzinfo))

# print()
# gap_time = datetime.datetime(2015, 10, 25, 1, 30, 0, 0)
# print('Gap time:', gap_time)
# print('Time since Gap time:', gap_time.timestamp())
# print()

# s = 1445733000
# t = s + (60 * 60)

# gb = pytz.timezone('GB')
# dt1 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(s)).astimezone(gb)
# dt2 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(t)).astimezone(gb)

# print("{} seconds since the epoch is {}".format(s, dt1))
# print("{} seconds since the epoch is {}".format(t, dt2))


# ================CHALLENGE==================
# Create a program that allows a user to choose one of
# up to 9 time zones from a menu. You can choose any
# zones you want from the all_timezones list.
#
# The program will then display the time in that timezone, as
# well as local time and UTC time.
#
# Entering 0 as the choice will quit the program.
#
# Display the dates and times in a format suitable for the
# user of your program to understand, and include the
# timezone name when displaying the chosen time.

available_zones = {'1': "Africa/Tunis",
                   '2': "Asia/Kolkata",
                   '3': "Australia/Adelaide",
                   '4': "Europe/Brussels",
                   '5': "Europe/London",
                   '6': "Japan",
                   '7': "Pacific/Tahiti",
                   '8': "US/Hawaii",
                   '9': "Zulu"}


while True:
    print("Please choose a time zone (or 0 to quit):")
    for place in sorted(available_zones):
        print("\t{}. {}".format(place, available_zones[place]))
    choice = input()

    if choice == '0':
        break

    if choice in available_zones.keys():
        tz_to_display = pytz.timezone(available_zones[choice])
        world_time = datetime.datetime.now(tz=tz_to_display)
        print("The time in {} is {} {}".format(available_zones[choice], world_time.strftime('%A %x %X %z'),world_time.tzname()))
        print("Local time is {}".format(datetime.datetime.now().strftime('%A %x %X')))
        print("UTC time is {}".format(datetime.datetime.utcnow().strftime('%A %x %X')))
        print()
