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

# creating appropriate outfiles for QGIS
utm18n = 26918
out_file = 'leadpoints.gpkg'
out_file_3 = 'crime.gpkg'

# This will match lead violations by first converting to CRS & the correct time coordinate system for north America
lead_violations = gpd.read_file("Lead_Violations_Data-shp.zip")
lead_violations = lead_violations.to_crs(epsg=utm18n)
lead_violations.to_file(out_file, layer='points', index=False)

# Doing the same thing for crime data records
crime = gpd.read_file("crimeshape.zip")
crime = crime.to_crs(epsg=utm18n)
crime.to_file(out_file_3, layer='points', index=False)

# Adding the block groups of Syracuse 
output_block = 'block.gpkg'
block = gpd.read_file('Census_Block_Group.zip')
block = block.to_crs(epsg=utm18n)
block.to_file(output_block, layer='points', index=False)

# Joining crime data to the block groups 
joined = crime.sjoin(block, how="left", predicate="within")
joined = joined.groupby("BLKGRPCE10")
maybe = joined.add_suffix("_Count").reset_index()
print(maybe)
output_joined = 'joined.gpkg'
#joined = joined.to_crs(epsg=utm18n)
joined.to_file(output_joined, layer='points', index=False)




 