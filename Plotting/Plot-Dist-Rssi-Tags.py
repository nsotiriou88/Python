# -*- coding: utf-8 -*-
"""
Created on Thu July 5 11:05:07 2018

@author: Nicholas Sotiriou - github: @nsotiriou88
"""

import os
import psycopg2
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import json
import pandas as pd


#%% Extract data for session
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

    query = "SELECT * FROM processed_packets WHERE session_id="+str(sess)+" ORDER BY timestamp"
    outputquery = "COPY ({0}) TO STDOUT WITH CSV HEADER".format(query)
    with open('dataset.csv', 'w') as file:
        curs.copy_expert(outputquery, file)
    print('\nFinished exporting data.')

    # Close connection to database
    curs.close()
    conn.close()
    
    
#%% Load data from file
with open('dataset.csv', 'r') as file:
    dataframe = pd.read_csv(file)

startTime = dataframe.iloc[0][1]

#Fill in the Tag & Anchor Lists
tagList = dataframe.tag_id.unique()
with open('anchors.json', 'r') as file:
    anchorsDict = json.load(file)
anchorList = [x for x in anchorsDict.keys() if x != '0x0']

#Tags dictionary of packet lists
tagsDict = {}
for tag in tagList:
    tagsDict[tag] = []
tagsExp = pd.DataFrame(data=dataframe, columns=['timestamp', 'tag_id', 'meas', 'imu_raw'])
tagsExp = tagsExp.iloc[:, :].values
for packet in tagsExp:
    tagsDict[packet[1]].append(packet)


# Packets from all Tag in dictionary
for tag, tagVal in tagsDict.items():    
    #Create a dictionary of lists for all the anchors and master.
    anchorDict = {}
    for anchor in anchorList:
        anchorDict[anchor] = {"timestamp":[], "rssi":[], "dist":[]}

    for packet in tagVal:
        try:
            data = json.loads(packet[2])
        except:
            continue
        for anchor in data:
            anchorDict[anchor['anchor']]['timestamp'].append(packet[0]-startTime)
            anchorDict[anchor['anchor']]['dist'].append(anchor['dist'])
            anchorDict[anchor['anchor']]['rssi'].append(anchor['rssi'])

    #Check the longer time that there were no comms
    for anchor, anchorVal in anchorDict.items():
        longerTime = 0.0
        timePtP = []
        for t in range(1, len(anchorVal['timestamp'])):
            timePtP.append(anchorVal['timestamp'][t] - anchorVal['timestamp'][t-1])
            if (anchorVal['timestamp'][t] - anchorVal['timestamp'][t-1]) > longerTime:
                longerTime = anchorVal['timestamp'][t] - anchorVal['timestamp'][t-1]
        
        avgTimePtP = np.mean(np.asarray(timePtP))
        print(tag, anchor)
        print(avgTimePtP)
        print(longerTime)
        print()

        #Convert lists to numpy arrays
        xTime = np.asarray(anchorVal['timestamp'])
        yDist = np.asarray(anchorVal['dist'])
        yRssi1 = np.asarray(anchorVal['rssi'])
        
        #########  Plotting graphs  #########
        # Distance
        if len(yDist) == 0 or len(yDist) == 1:
            continue
        plt.subplot(211)
        plt.plot(xTime, yDist, 'ro', xTime, yDist, 'b--')
        plt.title('Tag '+tag+' to Anchor '+anchor+' - Dist')
        plt.xlabel('Time(s) - Longer time between packets: '+repr(longerTime))
        plt.ylabel('Distance - red color are the points')
        plt.grid(True)
        
        # RSSI
        plt.subplot(212)
        plt.plot(xTime, yRssi1, 'ro', xTime, yRssi1, 'b--')
        plt.title('Tag '+tag+' to Anchor '+anchor+' - Rssi1')
        plt.xlabel('Time(s) - Longer time between packets: '+repr(longerTime))
        plt.ylabel('RSSI - red color are the points')
        plt.grid(True)

        #Save Plots and clear the plotter
        fig = plt.gcf()
        fig.set_size_inches((21, 9), forward=False)
#        if anchor == '0x78C':
#            fig.savefig('Tag'+tag+'Anchor'+anchor+'.png', dpi=100)
        fig.savefig('Tag'+tag+'Anchor'+anchor+'.png', dpi=100)
        plt.close()



#plt.show()
