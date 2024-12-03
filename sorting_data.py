#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 16:19:37 2024

@author: jadepaolillo
"""

import pandas as pd
import os

# file path and reading the file
metadata_dir = "/Users/jadepaolillo/manim/metadata_csv/metato2023.csv"
season_dir = "/Users/jadepaolillo/manim/season_csv/seasonto2023.csv"
dfs = pd.read_csv(season_dir)
df = pd.read_csv(metadata_dir)

# Make 'event_date' to be in the datetime format
df['event_date'] = pd.to_datetime(df['event_date'])
dfs['event_date'] = pd.to_datetime(dfs['event_date'])
metatosort = df.columns[-1]
seasontosort = dfs.columns[-1]
# sort df by 'event_date'
df_sorted = df.sort_values(by=metatosort)
dfs_sorted = dfs.sort_values(by=seasontosort)
df_sorted = df.sort_values(by='event_date')
dfs_sorted = dfs.sort_values(by='event_date')

# save to a new file
sorted_meta = "/Users/jadepaolillo/manim/metadata_csv/sortedmetato2023.csv"
sorted_season = "/Users/jadepaolillo/manim/season_csv/sortedseasonto2023.csv"
df_sorted.to_csv(sorted_meta, index=True)
dfs_sorted.to_csv(sorted_season, index=True)

# open the new dataframes for merging into one large frame
sorted_meta_df = pd.read_csv(sorted_meta)
sorted_season_df = pd.read_csv(sorted_season)

# Align the two sorted DataFrames by 'tm_market' and 'event_date' keys
aligned_sorted_df = pd.merge(sorted_season_df, sorted_meta_df, 
                    on=['tm_market', 'event_date'], 
                    suffixes=('_season', '_meta'))

# Save the merged and aligned large dataset to its own csv
aligned = "/Users/jadepaolillo/manim/Alignednfl.csv"
aligned_sorted_df.to_csv(aligned, index=True)

print(aligned_sorted_df.head())

