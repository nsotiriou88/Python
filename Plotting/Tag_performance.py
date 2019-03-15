# -*- coding: utf-8 -*-
"""
Created on Thu July 5 11:05:07 2018

@author: Nicholas Sotiriou - github: @nsotiriou88
"""

# Importing the libraries
import numpy as np
import json
import matplotlib.pyplot as plt
import pandas as pd
import csv
from scipy import signal
import psycopg2
import os
import sys
import matplotlib
matplotlib.use('Agg')


# %% Extract data if needed
extract = input('\nNeed to extract data? (y/n):')
extract = extract.lower()
with open('database_conn.json', 'r') as file:
    database_list = json.load(file)
    target_ip = ''
if extract == 'y':
    try:
        # Choose Database
        db_keys = list(database_list.keys())
        db_keys.sort(key=int)
        while target_ip not in db_keys:
            for key in db_keys:
                print('\t'+'('+key+') \t'+database_list[key]["name"]+'. - IP: ('+database_list[key]["ip"]+')')
            target_ip = input('\nPlease select database to connect: ')

        # Obtain Password for database
        try:
            password = os.environ['SPORTABLEDB']
        except:
            password = input("\nPlease set the environment variable SPORTABLEDB or give Database password: ")

        # Trying to connect to database
        conn = psycopg2.connect(host=database_list[target_ip]['ip'], database=database_list[target_ip]['db_name'], user="metrics_server", password=password, port=database_list[target_ip]['port'])
    except:
        print("Unable to connect to the database. Please try again.")
        sys.exit(0)
    curs = conn.cursor()
    query = "SELECT id, start_time, end_time, name FROM sessions ORDER BY start_time DESC LIMIT 100"
    curs.execute(query)
    res = curs.fetchall()
    print('The last 100 sessions are:\n')
    count = 0
    recorded_session_ids = []
    for line in res:
        count += 1
        print('\t'+'('+str(count)+') '+line[3]+',\tDURATION: '+str((line[2]-line[1])//60)+'mins,\tID: '+str(line[0]))
        recorded_session_ids.append(line[0])
    sess = input('\nPlease Choose the Number of the Session to Process: ')
    sess = recorded_session_ids[int(sess)-1]

    # query = "SELECT * FROM processed_packets WHERE session_id="+str(sess)+" ORDER BY timestamp"
    query = "SELECT * FROM processed_packets WHERE session_id="+str(sess)+" AND (x<>0.0 AND y<>0.0) ORDER BY timestamp"
    outputquery = "COPY ({0}) TO STDOUT WITH CSV HEADER".format(query)
    with open('dataset.csv', 'w') as file:
        curs.copy_expert(outputquery, file)
    print('\nFinished exporting data.')

    # Close connection to database
    curs.close()
    conn.close()


#%% Aquire a list of tags for the session
#df = pd.read_csv('dataset.csv', delimiter=',', encoding="ISO-8859-1")
df = pd.read_csv('6 anchor replaced 2.csv', delimiter=',', encoding="ISO-8859-1")
tags = df.tag_id.unique()

#%% Data processing for each player
# Importing the dataset
count = 0
outputFile = {}  # Keep averages for csv exporting

for tag in tags:
    count += 1

    dataset = df.loc[df['tag_id'] == tag]
    tag1 = dataset.iloc[:, [0, 1]].values
    first_timestamp = tag1[0][1]

    # Calculate packets per second and average of session
    tag1[:, 1] -= first_timestamp
    total_tag_packets = len(tag1)
    tag_duration = tag1[-1, 1]
    avg_packets_per_sec = total_tag_packets/tag_duration
    outputFile[tag] = round(avg_packets_per_sec,2)

    packets_per_sec = []
    for i in range(0, int(tag_duration)):
        packets_per_sec.append(((tag1[:, 1] >= i) & (tag1[:, 1] <= i+1)).sum())
    packets_per_sec = np.array(packets_per_sec)
    

    # ======= Plotting Stuff =======
    plt.clf()

    # Plot only when applying filters
    packet_time = np.linspace(0, len(packets_per_sec)-1, len(packets_per_sec))
    plt.plot(packet_time/60, packets_per_sec, 'b-', linewidth = 0.8, label='Packets per sec - '+tag+' - Average Packets: '+str(round(avg_packets_per_sec, 2))+'p/s')

    plt.title(tag+' - Tag Performance')
    plt.xlabel('time (m)')
    plt.ylabel('reported packets', rotation='vertical')
    plt.legend()
    plt.grid(linestyle='--', linewidth=1)

#    plt.show()
    plt.gcf().set_size_inches((21, 9), forward=False)
    plt.savefig(tag+'.png', dpi=100, format='png', bbox_inches='tight')
    print('\nFinished plotting data for Player:', tag+'-'+tag, str(count)+'/'+str(len(tags)))
#    if tag == tags[1]:
#        break  #DEBUG ==========================

#%% Export results to csv
with open('tag_perf.csv', mode='w') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['Tag ID', 'Average Packets per sec'])
    for tag in tags:
        line = [tag, outputFile[tag]]    
        writer.writerow(line)
