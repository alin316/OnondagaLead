#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 23:24:46 2022

@author: annalin
"""

import geopandas as gpd , fiona
import pandas as pd 
from geopandas import GeoSeries
from shapely.geometry import Point, Polygon

utm18n = 26918
out_file = 'leadpoints.gpkg'
out_file_2 = 'elementary.gpkg'
out_file_3 = 'crime.gpkg'

lead_violations = gpd.read_file("Lead_Violations_Data-shp.zip")
lead_violations = lead_violations.to_crs(epsg=utm18n)
lead_violations.to_file(out_file, layer='points', index=False)

elementary = gpd.read_file("tl_2020_36_elsd.zip")
elementary = elementary.to_crs(epsg=utm18n)
elementary.to_file(out_file_2, layer='points', index=False)

crime = gpd.read_file("crimeshape.zip")
crime = crime.to_crs(epsg=utm18n)
crime.to_file(out_file_3, layer='points', index=False)

output_block = 'block.gpkg'
block = gpd.read_file('Census_Block_Group.zip')
block = block.to_crs(epsg=utm18n)
block.to_file(output_block, layer='points', index=False)

#print(block)
#print(crime)
#print(block.keys())
#print(crime.keys())
joined = crime.sjoin(block, how="left", predicate="within")
joined = joined.groupby("BLKGRPCE10")
maybe = joined.add_suffix("_Count").reset_index()
print(maybe)
output_joined = 'joined.gpkg'
#joined = joined.to_crs(epsg=utm18n)
joined.to_file(output_joined, layer='points', index=False)
#print(joined.first())
#joined.groupby("")
#print(joined)
#print(joined.keys())
# group by on the block[crime]
'''
onabonubaga.crs = 26918
#lead_violations.crs = "ESPG:26918"
#lead_violations = lead_violations.set_crs(epsg=utm18n)
#lead_violations.to_file(out_file, layer='rings', index=False)

geo = []
for i in range(0, len(lead_violations)):
    #poly_start = GeoSeries(Point(float(lead_violations["X"][i]),
      #                 float(lead_violations["Y"][i])))
    geo.append(Point(float(lead_violations["X"][i]),
                       float(lead_violations["Y"][i])))
df = gpd.GeoDataFrame() 
df['geometry'] = geo


df = df.set_crs(utm18n)

df.set_geometry(col='geometry', inplace=True)
df.to_file(out_file, layer='rings', index=False)
onabonubaga.to_file("new_onondaga.gpkg")

#for i in lead_violations:
    '''
    

 