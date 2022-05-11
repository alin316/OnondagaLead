# Syracuse Lead Violation & Crime Data Visualization

# Intro
This repository is about analyzing the lead violation and crime data provided by the City of Syracuse. What I wanted to do with this data was to visualize it via GQIS Mapping. I thought that visual information was the best way to present my analysis to the general public. 

# Inputs
The main inputs of this repository were: 

Census_Block_Groups_in_Syracuse%2C_NY_(2010).csv
  Found exaclty using this URL: https://data.syrgov.net/maps/bcb791612199446cbacb14b0ef44aff5
  
Lead_Violations_Data.csv & Shape file 
  Found exaclty using this URL: https://data.syrgov.net/datasets/79a29e96092840168849bebcce7addf2_0/explore?location=43.034457%2C-76.147037%2C13.58
  
crime_data.csv & Shape file: 
  Found exactly using this URL: https://data.syrgov.net/datasets/d3c98278e2864a2bbcd00e6e30358856_0/explore?location=43.035505%2C-76.140695%2C13.88
  
onondaga.gpkg (taken from previous assigments) 

projectcode.py (Script #1) 

count_code.py (Script #2)

# Discussion
The 2022 Crime Data Part 1 information provided by the city of Syracuse contains 219 Records. The 2020 Lead Data provided by the Onondaga County 1307 records. 

After analyzing the crime data, this was the breakdown of the different types of crimes. 

![pie_plog](https://user-images.githubusercontent.com/98330114/167912055-5a2fc665-a86d-4649-ae70-9fbba5bd74c1.png)

Next, is a QGIS Map of each crime record and lead violation record plotted according to the location. There are some points outside of the City of Syracsue in Onondaga County (Author Note: I attempted to edit those points out but Adobe Illustrator was unable to do that)


[basicmap.pdf](https://github.com/alin316/OnondagaLead/files/8672303/basicmap.pdf)


# Python Outputs 
leadpoints.gpkg,
pie_plog.png,
crime.gpkg, 
joined.gpkg 

# QGIS Outpus 
basicmap.pdf,
leadmap.pdf

# Other Info
It does not matter as to what order the scrips are run.
The output files are going to be crime.gpkg and lead.qgzpoints that indicate how many occurances of an incident so there are no units. 
joined.pgkg is going to plot the lead points correcly on to the block groups of Syracuse 
