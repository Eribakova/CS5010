# CS5010 Final Project

Jenny Jang, 
Carol Moore, 
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

### Experimental Design

REQUIRED: Experimental Design: Describe briefly your process, starting from where you obtained your data all the way to means of obtaining results/output. 
Beyond the original specifications: Highlight clearly what things you did that went beyond the original specifications. That is, discuss what you implemented that would count toward the extra-credit portion of this project (see section below).

### Key results

REQUIRED: Results: Display and discuss the results. Describe what you have learned and mention the relevance/significance of the results you have obtained.

## Bike sharing usage us down during COVID-19

It is not surprising, that bike sharing fell throughout 2020 due to COVID-19. As infections picked up and lockdowns were announced, bike sharing dropped off and failed to pick up to the pre-COVID levels even by the end of 2020. It is notable that data suggests that people began taking precautions even before official lockdowns were introduced. 

![image](https://user-images.githubusercontent.com/70774260/117549581-37113180-b009-11eb-8da3-1cbdb78c3b52.png)

## Bike sharing during commuting hours is sharply down

Trips for 2020 as a whole shifted from commuting hours to what seems to be leisure hours (afternoons and evenings). However, the change did not occur immediately. Trips were down throughout the day in March 2020 compared to March 2019.  However, there were still a lot of trips during commuting hours. By June, commuting hour trips were much lower than in 2019 and late afternoon trips were up. The finding seems to suggest that after the lockdowns in April, more people might have settled into working from home, but continued to use bike share, this time for leisure

![image](https://user-images.githubusercontent.com/70774260/117549626-7b043680-b009-11eb-9f79-b39dab864536.png)




### Testing of our program 

REQUIRED: Testing: Describe what testing you did. Describe the unit tests that you wrote. Show a sample run of 1 or 2 of your tests (screen captures or copy-and-paste is fine).

We use method-based unit testing for our data cleaning part as well as the data analysis part. We are incorporating our testing into our Jupiter notebook code. We focused mostly on assert tests that our data transformation and aggregation in the process of cleaning and preparing the dataset produces the expected results in the final clean dataset. Below are a few examples of the tests we performed. 
* We checked that our lat/long information is correctly matched to stations where it was missing (earlier part of the data sample). 
* We recalculated the duration of the trip and made sure it is correctly reflected in our dataset. 
* We used assert statements to make sure time groups were correct. 

![image](https://user-images.githubusercontent.com/70774260/117549451-755a2100-b008-11eb-8d02-80fb248964ce.png)


### Conclusions

REQUIRED: Conclusions: Summarize your findings, explain how these results could be used by others (if applicable), and describe ways you could improve your program. You could describe ways you might like to expand the functionality of your program if given more time.

We used high frequency information on bike sharing before and after the onset of COVID-19 in DC metropolitan area, focusing on VA specifically. We found that the overall usage of bike sharing has dropped off significantly as the rate of infections picked up. It appears that the use began to fall off already in February, even before the official lockdowns, possibly as people began taking precautions ahead of the official announcements.

While it was not surprising that we found that bike sharing related to commuting (as seen by day and time of usage) fell, as more persons were required or opted to work from home, we were surprised to find that leisure related biking has increased. People took longer trips, including during lunchtime or afternoon hours during weekdays and on the weekends. Bike trips originating from parks or tourist attractions also picked up. 

Public health care officials could use our findings to disseminate information on precautions of using shared resources outdoors during COVID-19. By monitoring frequency of trips during certain days or hours of the day, they can adjust road closures, particularly on the weekends, to relieve bike congestion. They could also use this information to place strategically information and sanitizing equipment at the stations that are most frequently used and adjust it accordingly as people return to work and commuting biking begins to return. 

![image](https://user-images.githubusercontent.com/70774260/117548484-442b2200-b003-11eb-8f06-c2fb24eadbf0.png)

In our future work we would like to improve mapping functionality, where we can see on a map the most frequently used stations during different times of day or hour. This way it will be easier for public sector government officials to assess when and where to dedicate more resources to bike sharing and public education campaigns on risks using shared resources outdoors during COVID-19. 


### References

In addition to CS5010 class resources we used the following references

https://dtkaplan.github.io/DataComputingEbook/index.html#table-of-contents

https://towardsdatascience.com/visualizing-bike-mobility-in-london-using-interactive-maps-for-absolute-beginners-3b9f55ccb59

https://towardsdatascience.com/exploring-bike-share-data-3e3b2f28760c

https://towardsdatascience.com/applied-exploratory-data-analysis-the-power-of-visualization-bike-sharing-python-c5b2645c3595




