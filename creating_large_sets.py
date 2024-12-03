#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 16:02:18 2024

@author: jadepaolillo
"""

import pandas as pd
import os

metadata_dir = "/Users/jadepaolillo/manim/metadata_csv"
season_dir = "/Users/jadepaolillo/manim/season_csv"

metadata = []
season = []

# read and adds all of CSV in the dir
for file in os.listdir(metadata_dir):
    if file.endswith('csv'):
        file_path = os.path.join(metadata_dir, file)
        df = pd.read_csv(file_path)
        metadata.append(df)
for file in os.listdir(season_dir):
    if file.endswith('csv'):
        file_paths = os.path.join(season_dir, file)
        dfs = pd.read_csv(file_paths)
        season.append(dfs)
        

# the combination of the frames
metato2023 = pd.concat(metadata, ignore_index=False)
seasonto2023 = pd.concat(season, ignore_index=False)

# Save the frame to its own CSV
metato2023.to_csv('/Users/jadepaolillo/manim/metadata_csv/metato2023.csv', index=False)
seasonto2023.to_csv("/Users/jadepaolillo/manim/season_csv/seasonto2023.csv", index=False)

