#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 22:38:15 2022

@author: annalin
"""
import csv
import matplotlib.pyplot as plt
crimes ={}


file = open('crime_data.csv')
csvreader = csv.reader(file)

for x in csvreader: 
   if x[5] in crimes.keys():
       crimes[x[5]] += 1
   else: 
       crimes[x[5]] = 1
print(crimes)
    
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = list(crimes.keys())[1:]
sizes = list(crimes.values())[1:]
explode = (0, 0, 0, 0, 0, .2)  

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()  
    
# dict
# dict["a"] = 0
# dict["apple"] = 1
# dict["apple"] += 1
# dict["banana"] = 1
# if "apple" in dict.keys():
    # dict["apple"] += 1
# else
# dict["apple"] = 0
