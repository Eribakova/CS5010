# CS5010 Final Project

Jenny Jang
Carol Moore
Elina Ribakova 

## BikeShare Data Analysis comparing pre-covid and post-covid

<img src="https://github.com/Eribakova/CS5010/blob/main/Bike.PNG">

### Introduction

We wanted to explore some idea on how people's social behavior changed with covid. Our focus is on a change of trend in bikesharing. Here are some example questions we thought to find out:

1. Did the number of trips change from pre-COVID and post-COVID?
2. Did any COVID even change the bikeshare frequency?
3. Comparison between suburb area and city area.


### Introducing our DATASET

We got our dataset from 'Capital Bikshare', from following website: https://www.capitalbikeshare.com/system-data
For our project, we concatenated monthly dataset from  February 2019 to March 2021. We then merged in data on COVID-19 cases and deaths since March 2020.

### Data cleaning

The data set included numerous inconsistencies and missing values that had to be remedied prior to analysis.  For example, column headings and formats differed for files before and after May 2020.  We ran each monthly dataframe through a for-loop to standardize headings, which allowd the files to be concatenated.  Latitude and longitude data, necessary for mapping, were missing for files dated prior to May 2020.  We developed a dictionary that mapped station id to lat/long, which we used to interpolate the missing data.  We found that lat/long data were not standard, differing in the number of decimal places, resulting in over 48,000 unique lat/longs for only 600 stations.  After standardizing the lat/longs, we ran a reverse geocode library, geopy, to extract state and county.  The breakdown of state is shown below:

 District of Columbia:  4,892,84
 Virginia:  590,687
 Maryland: 135,035
 NaN: 119,252

Based on this information we decided to limit the project Virginia only, so that the final dataset consistes of 590,687 bikesharing trips that started in Northern Virginia.

### Testing of our program 

We use method-based unit testing for our data cleaning part as well as the data analysis part. We are incorporating our testing into our Jupiter notebook code. We focused mostly on assert tests that our data transformation and aggregation in the process of cleaning and preparing the dataset produces the expected results in the final clean dataset. Below are a few examples of the tests we performed. 
* We checked that our lat/long information is correctly matched to stations where it was missing (earlier part of the data sample). 
* We recalculated the duration of the trip and made sure it is correctly reflected in our dataset. 

### Planned Queries

Many cities reported a spike in bicycle sales and bike sharing.  Although public health regulations and concerns may have kept many people confined, many experienced an increase in leisure time or flexibity.  With businesses closed, some turned to outdoor activity for recreation.  In Illinois, the bike share system "set monthly ridership records in August, September, and October, while many bike shops are experiencing unprecedented demand." (Chicago Metropolitan Agency for Planning (CMAP), "Pandemic presents opportunity for communities to embrace biking and walking," website post, undated).  Areas with tourism, such as Washington DC, may have expercienced a similar boom in cycling that was offset by having fewer visitors.  Our queries focus on comparing bikesharing patterns before March 2020 with patterns afterward.  

1. How did the number of trips change?  For example, did Northern Viriginia see an increase in ridership similar to Illinois or was there a decrease given the reduced number of visitors to the area and the State lockldown?
2. Were there changes in the duration and time of day of bike shares?  Can we gain insight into whether people were using bikes for commuting, given less traffic on the roads?
3. Are there dips and increases following select public health events and information (e.g., first case reported in State?)
4. Is there a difference by town/county?  


### Findings so far





