#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 10:20:48 2024

@author: jadepaolillo
"""

import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np


# creating the data and all other necessary 
nfldata = "/Users/jadepaolillo/manim/Alignednfl.csv"
df = pd.read_csv(nfldata)
margin = []
tm_score = []
opp_score = []
tossoutcome = []
tmname = []
didtmwintoss = []
yes = []
no = []
# filling the scores and calculating margin of victory
for i in df['tm_score']:
    tm_score.append(i)
for i in df["opp_score"]:
    opp_score.append(i)
j = 0
k = 0

while j <= (len(tm_score) - 1):
    marg = tm_score[j] - opp_score[j]
    margin.append(marg)
    j = j+1

# filling team names and coin toss names
for i in df["won_toss"]:
    tossoutcome.append(i)
    
for i in df["tm_alias_meta"]:
    tmname.append(i)

# checking to see if the team who won the game won the toss
while k <= (len(tmname) - 1):
    if tmname[k] == tossoutcome[k]:
        didtmwintoss.append(1)
        k = k + 1
    else:
        didtmwintoss.append(0)
        k = k + 1

for i in range(len(didtmwintoss)):
    if didtmwintoss[i] == 1:
        yes.append(didtmwintoss[i])
    else:
        no.append(didtmwintoss[i])
        
label = ["won toss", "lost toss"]
size = [((len(yes)/len(didtmwintoss))*100), ((len(no)/len(didtmwintoss))*100)]
color = ["#1395ff","#ff1313"]
plt.pie(size, labels=label, colors=color, autopct='%1.1f%%')

plt.title("Does the Coin Toss lead to a Win?")
plt.show()
