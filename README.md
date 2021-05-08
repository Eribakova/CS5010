# CS5010 Final Project

Jenny Jang
Carol Moore
Elina Ribakova 

Github repository: https://github.com/Eribakova/CS5010

## BikeShare Data Analysis comparing pre-covid and post-covid

<img src="https://github.com/Eribakova/CS5010/blob/main/Bike.PNG">

### Introduction

REQUIRED: Introduction: Describe your project scenario. Starting out, what did you hope to accomplish/learn?

We wanted to explore how people's social behavior changed with Covid-19, particularly their activity outdoors. Many cities reported a spike in bicycle sales and bike sharing.  In Chicago “unprecedented demand” (*Chicago Metropolitan Agency for Planning (CMAP), "Pandemic presents opportunity for communities to embrace biking and walking," website post, undated*). 

What is the intended audience and what is the best use for our analysis? First, public healthcare officials could use this data to assess whether there has been a spike in leisure biking in the area and whether some of the trails are getting more congested than others. They could use this information to a) disseminate more information on safety precautions for biking outdoors, b) to post safety information posters at the stations that are most frequently used, c) place sanitizing equipment on the most frequent paths. Second, if biking activity has increased on the weekend, road police could consider closing part of the roads less used on the weekend by cars to dedicate them to bike use.    

In this project we performed month-to-month comparisons on Capital Bikeshare ridership to show to impact of the pandemic in the DC metro area, ultimately focusing on VA. We focused on the following key questions: 

1. Did the number of trips change from pre-COVID to post-COVID period?
2. Has COVID changed bikesharing behaviour in other ways?
3. Has leaisure-related biking increased versus commuting?


### Introducing our DATASET

REQUIRED: The Data: Describe your data set and its significance. Where did you obtain this data set from? Why did you choose the data set that you did? Indicate if you carried out any preprocessing/data cleaning/outlier removal, and so on to sanitize your data.

Our data is monthly on bike sharing data that provided trip data, by time, starting and ending location and address and ID of the starting and ending location station. In the most recent part of the dataset, longitude and latitude data for bike stations was also provided. We got our dataset from 'Capital Bikshare', from following website: https://www.capitalbikeshare.com/system-data. 

In addition, we used public health dataset from: https://data.virginia.gov/Government/VDH-COVID-19-PublicUseDataset-Cases/bre9-aqqr. The dataset provided information on hospitalizations and mortality rates by region in DC metropolitan area. 

For our project, we concatenated monthly bikesharing dataset from  February 2019 to March 2021 and then merged in data on COVID-19 cases and deaths since March 2020. 


### Data cleaning

The data set included numerous inconsistencies and missing values that had to be remedied prior to analysis. We identified missing data, irregular data (mixed formats and outliers, for example trips with over duration spanning multiple days, where likely someone did not return a bike), we dropped columns with unnecessary Data (data we were not planning to use or repetitive Data), and inconsistent Data ("negative" trip duration). We also needed to merge two datasets: one pertaining to bike share information and another to COVID-19 instances. 

In the bike share data, column headings and formats differed for files before and after May 2020. We ran each monthly dataframe through a for-loop to standardize headings, which allowed the files to be concatenated. Latitude and longitude data, necessary for mapping, were missing for files dated prior to May 2020. We developed a dictionary that mapped station id to lat/long, which we used to interpolate the missing data. We found that lat/long data were not standard, differing in the number of decimal places, resulting in over 48,000 unique lat/longs for only 600 stations. After standardizing the lat/longs, we ran a reverse geocode library, geopy, to extract state and county. The breakdown of state is shown below:

 District of Columbia:  4,892,84
 Virginia:  590,687
 Maryland: 135,035
 NaN: 119,252

Based on this information we decided to limit the project Virginia only, so that the final dataset consists of 590,687 bikesharing trips that started in Northern Virginia.

### Planned Queries

REQUIRED: Experimental Design: Describe briefly your process, starting from where you obtained your data all the way to means of obtaining results/output. 
Beyond the original specifications: Highlight clearly what things you did that went beyond the original specifications. That is, discuss what you implemented that would count toward the extra-credit portion of this project (see section below).

REUIRED: Results: Display and discuss the results. Describe what you have learned and mention the relevance/significance of the results you have obtained.
Testing: Describe what testing you did. Describe the unit tests that you wrote. Show a sample run of 1 or 2 of your tests (screen captures or copy-and-paste is fine).



Many cities reported a spike in bicycle sales and bike sharing.  Although public health regulations and concerns may have kept many people confined, many experienced an increase in leisure time or flexibity.  With businesses closed, some turned to outdoor activity for recreation.  In Illinois, the bike share system "set monthly ridership records in August, September, and October, while many bike shops are experiencing unprecedented demand." (Chicago Metropolitan Agency for Planning (CMAP), "Pandemic presents opportunity for communities to embrace biking and walking," website post, undated).  Areas with tourism, such as Washington DC, may have expercienced a similar boom in cycling among residents that was offset by having fewer visitors.  

Our queries focus on comparing bikesharing patterns before March 2020 with patterns afterward.  

1. How did the number of trips change?  For example, did Northern Viriginia see an increase in ridership similar to Illinois or was there a decrease given the reduced number of visitors to the area and the State lockldown?
2. Were there changes in the duration and time of day of bike shares?  Can we gain insight into whether people were using bikes for commuting, given less traffic on the roads?
3. Are there dips and increases following select public health events and information (e.g., first case reported in State?)
4. Is there a difference by town/county?  

<img src="https://github.com/Eribakova/CS5010/blob/main/Violin.png">


### Testing of our program 

We use method-based unit testing for our data cleaning part as well as the data analysis part. We are incorporating our testing into our Jupiter notebook code. We focused mostly on assert tests that our data transformation and aggregation in the process of cleaning and preparing the dataset produces the expected results in the final clean dataset. Below are a few examples of the tests we performed. 
* We checked that our lat/long information is correctly matched to stations where it was missing (earlier part of the data sample). 
* We recalculated the duration of the trip and made sure it is correctly reflected in our dataset. 

### Conclusions

REQUIRED: Conclusions: Summarize your findings, explain how these results could be used by others (if applicable), and describe ways you could improve your program. You could describe ways you might like to expand the functionality of your program if given more time.


![image](https://user-images.githubusercontent.com/70774260/117548429-ec8cb680-b002-11eb-823c-434038ea911d.png)



### References

In addition to CS5010 class resources we used the following references

https://dtkaplan.github.io/DataComputingEbook/index.html#table-of-contents

https://towardsdatascience.com/visualizing-bike-mobility-in-london-using-interactive-maps-for-absolute-beginners-3b9f55ccb59

https://towardsdatascience.com/exploring-bike-share-data-3e3b2f28760c

https://towardsdatascience.com/applied-exploratory-data-analysis-the-power-of-visualization-bike-sharing-python-c5b2645c3595




