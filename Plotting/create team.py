# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 10:45:07 2018

@author: Nicholas Sotiriou - github: @nsotiriou88
"""

import json
import pandas as pd


# Players ID-NAME
dataset = pd.read_csv('players.csv', delimiter = ',')
players = dataset.iloc[:, [0, 1]].values

# Players ID-tagID
dataset = pd.read_csv('players_session.csv', delimiter = ',')
players_session = dataset.iloc[:, [1, 3]].values

tags = {}
for i in range(len(players_session)):
    if players_session[i][1] not in tags:
        tags[players_session[i][0]] = players_session[i][1]

names = {}
for i in range(len(players)):
    if players[i][1] not in names:
        names[players[i][0]] = players[i][1]


tag_names = {}
for key, value in tags.items():
    tag_names[value] = names[key]

# JSON output of the tag_names
with open('tag_names.json', 'w') as file:
    json.dump(tag_names, file)
