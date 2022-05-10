#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 22:38:15 2022

@author: annalin
"""

import csv
import matplotlib.pyplot as plt
crimes ={}

# will open and read CSV file 
file = open('crime_data.csv')
csvreader = csv.reader(file)

# I am counting all the the variables in column 6 of this CSV file
# It will add to the dictionary and count all the different types of frimes 
for x in csvreader: 
   if x[5] in crimes.keys():
       crimes[x[5]] += 1
   else: 
       crimes[x[5]] = 1
print(crimes)
    
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = list(crimes.keys())[1:]
sizes = list(crimes.values())[1:]
# .2 means that the last slice will be sticking out a bit compared to the rest. 
explode = (0, 0, 0, 0, 0, .2)  

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()  
    

