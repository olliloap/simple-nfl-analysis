#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 11:24:21 2024

@author: jadepaolillo
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

nfldata = "/Users/jadepaolillo/manim/Alignednfl.csv"
df = pd.read_csv(nfldata)

# splits the data by year
seasongroups = df.groupby("season_season")

homewinper = []

# getting the # of wins per season at home
for season, group in seasongroups:
    total_games = len(group)
    home_games = group[group["tm_location"] == "H"]
    home_win_count = len(home_games)
    
    # percent of home wins
    if total_games > 0:
        homewinper.append((home_win_count/total_games)*100)
    else:
        homewinper.append(0)
        
averageatt = []

# getting the average attendance per season
for season, group in seasongroups:
    total_games = len(group)
    attendance = group["attendance"].sum()
    if total_games > 0:
        averageatt.append((attendance/total_games))
    else:
        averageatt.append(0)


maximumatt = max(averageatt)
stdatt = []
i = 0

# creates a standardized attendence based on the max average then makes
# it a percentage so I can compare to the win percentage at home
while i < len(averageatt):
    standard = (averageatt[i] / maximumatt) * 100
    stdatt.append(standard)
    i = i + 1

fixedstdatt = []
fixedyears = []
years = list(range(2000, 2024))

# removal of the outliers and placing in new lists
for j, value in enumerate(stdatt):
    if value > 50:
        fixedstdatt.append(value)
        fixedyears.append(years[j])
# linear regression
modelwin = LinearRegression()
modelatt = LinearRegression()
# turns the years array to be vertical not horizontal like a list
years1 = np.array(years).reshape(-1, 1)
modelwin.fit(years1, homewinper)
# Gives me the line of best fit for win percentage
line_of_best_fit_win = modelwin.predict(years1)

# same as above but with the stdatt to get a linear regression
fixedyears1 = np.array(fixedyears).reshape(-1, 1)
modelatt.fit(fixedyears1, fixedstdatt)
line_of_best_fit_att = modelatt.predict(fixedyears1)

# created the x values for all graphs
x = np.linspace(2000, 2023, 24)
labels = ["Home Win Percentage", "Standardized Average Attendence",
          "Standardized Average Attendence w/o Outlier", "Line of Best Fit"]

# plot of home win percentage alone
plt.figure(figsize=(10,6))
plt.plot(x, homewinper, color = "#000000", label = labels[0])
plt.plot(years1, line_of_best_fit_win, color = "#ff0000", label = labels[3], 
         linestyle = "dotted")
plt.grid(True)
plt.ylabel("% of Wins if the Team is at Home (%)")
plt.xlabel("Year starting at 2000")
plt.title("Home Field Advantage")
plt.legend()
plt.show()
  
# plot of standardized average attendance
plt.figure(figsize = (10,6))
plt.plot(x, stdatt, color = "#ff0000", label = labels[1])
plt.grid(True)
plt.ylabel("Average Attendance Standardized to Maximum Average (%)")
plt.xlabel("Year Starting With 2000")
plt.title("Standardized Attendence per Year")
plt.legend()
plt.show()

# plot of stdatt without 2020, the outlier
plt.figure(figsize = (10,6))
plt.plot(fixedyears, fixedstdatt, color = "#000000", label = labels[2])
plt.plot(fixedyears1, line_of_best_fit_att, color = "#ff0000", 
         label = labels[3], linestyle = "dotted")
plt.grid(True)
plt.ylabel("Average Attendance Standardized to Maximum Average (%)")
plt.xlabel("Year Starting With 2000")
plt.title("Standardized Attendence w/o 2020 per Year")
plt.legend()
plt.show()

# plot of both to see if any trends appear
plt.figure(figsize = (10,6))
plt.plot(x, homewinper, color = "#000000", label = labels[0])
plt.plot(fixedyears, fixedstdatt, color = "#ff0000", label = labels[2])
plt.grid(True)
plt.ylabel("Percentage (%)")
plt.xlabel("Year Starting With 2000")
plt.title("Home Win Percentage vs. Average Attendence")
plt.legend()
plt.show()


    
    
    