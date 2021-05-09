# CS5010 Final Project

Jenny Jang, 
Carol Moore, 
Elina Ribakova 

Github repository: https://github.com/Eribakova/CS5010

## Bike-Sharing: Insight into Public Precautions During the COVID-19 Pandemic

<img src="https://github.com/Eribakova/CS5010/blob/main/Bike.PNG">

## Objectives

We wanted to explore how people's social behavior changed with COVID-19, particularly their activity outdoors.  In the Washington DC area, there were mixed policies about outdoor social gatherings.  Many parks were closed throughout the summer. However, recreational pathways remained open even when social distancing was difficult if not impossible, and the major DC area trails remained crowded and even broke weekend records for usage in March 2020. We examined the public's use of rental bikes to guage how the public took precautions or increased their risks during course of the pandemic. 

Many cities reported a spike in bicycle sales and bike sharing. For example, Chicago reported “unprecedented demand” in its bike-sharing system.  We wanted to see if the Washington DC area experienced a similar spike or if public health restrictions and precautions - which led reduced tourism and commuting -- caused a net reduction in usage, mitigating the potential risks of biking on narrow paths and on roads.

Our central analytic question is whether bikesharing declined in Virginia. To what extent did the number of trips change?  Did the pandemic foster a boom in demand like in Chicago?  Or, did bikesharing in DC decline in response to public health concerns and restrictions?  If the public were consistently taking increased precautions in all aspects of their public behavior we would expect to see bikesharing decrease and for trips to be shorter, especially in more crowded areas.   

Our analysis provides an example of how transactional commercial data can be used in urban planning and public health policy.  With regard to the latter, healthcare officials could use our data to assess potential risks associated with outdoor recreational behavior and to tailor interventions in addition to sanitizing equipment (which DC's bikesharing company, Capital Bikeshare, did).  These could include posting safety information posters at the bikesharing stations that are most frequently used, requiring a review of social distancing guidelines as part of the terms of the rental, emphasizing teh value of mask wear for outdoor recreation, or limiting rentals where social distancing is not possible. If merited, urban planners could use this information assess which roads might be closed on weekends to promote fitness and recreation, while enabling more social distancing than is possible on trails.  

## Data set

We used Capital Bikeshare’s Trip History dataset which is licensed for public use by Motivate, the company that operates Capital Bike share on behalf of Washington, DC area municipalities.  Capital Bikeshare maintains over 4,300 bikes across DC, Maryland and Northern Virginia and is the dominant bike sharing company in the region.  The data are available at https://www.capitalbikeshare.com/system-data. 

OWe downloaded 25 monthly data files from February 2019 to March 2021, the most recent file available.  

Each record is a trip from a starting kiosk, or station, to an end station.  Data fields include starting and ending station address, a date-timestamp (year-month-day-hour-minute-second) and the type of renter, e.g., casual or membership.  In the most recent part of the dataset, longitude and latitude data for bike stations was also provided. 

We wanted to examine bike sharing against the backdrop of events and new information during the pandemic.  Public health data provided the necessar context. We obtained epidemological data from https://data.virginia.gov/Government/VDH-COVID-19-PublicUseDataset-Cases/bre9-aqqr. The dataset provided information on hospitalizations and mortality rates by region in DC metropolitan area. These data were merged in with the bikeshare data to complete our file.

## Data Pipeline

### Preprocessing

In order to combine the 25 monthly bike share files into a single data set, we assessed if there were inconsistencies in the structure of the files over time.  We found that column headings and formats differed for files before and after May 2020. In most cases, however, the file format differences were not signiificant.  We ran each monthly dataframe through a for-loop to standardize headings, which allowed the files to be concatenated, resulting in a file of over 5.5M records.  The Python code for preprocessing is in the file datacleaning.ipynb.

#### Figure 1.  Standardizing column headings
![image](https://user-images.githubusercontent.com/70774260/117550168-ccfa8b80-b00c-11eb-9731-bbc6930c5a46.png)

#### Figure 2.  Merging Public Health Data
![image](https://user-images.githubusercontent.com/70774260/117550185-ed2a4a80-b00c-11eb-85e2-c14fe658900e.png)

### Cleaning

The bike share data set included numerous irregularities and missing values that had to be remedied prior to analysis. We eliminated trips with outlying durations spanning multiple days, where likely someone did not return a bike).

The data set had street address information but lacked city and state, aggregates that we believed would be more closely tied to public health regulations and that would be more tractable to work with.  We used the Python GEOPY library to extract city and state from the latitutde and longitude.  There were several issues which we solved in the following ways.

#### Figure 3.  Raw address data
![image](https://user-images.githubusercontent.com/70774260/117550233-38445d80-b00d-11eb-8a8e-e16fbdd0184d.png)

1.  Lat/long data were not standard, differing in the number of decimal places.  This resulted, for example, in over 48,000 unique lat/longs for only 600 stations during March 2021. The reverse gecode runtime totaled over 3 hours for one month's data.  Our solution was to take the mean lat-long to the 6th digit grouped by station id.  standardizing the lat/longs, we ran a reverse geocode library, geopy, to extract state and county. The breakdown of state is shown below:

 District of Columbia:  4,892,84
 Virginia:  590,687
 Maryland: 135,035
 NaN: 119,252

Based on this information we decided to limit the project Virginia only, so that the final dataset consists of 590,687 bikesharing trips that started in Northern Virginia.

## Experimental Design

In this section, we discuss how we analyzed the data.  The analysis and visualization code is primarily in the file monthtomonth.ipynb.

Our approach was to compare bike sharing patterns 'pre-COVID' and 'post-COVID'.  Because bicycling is a seasonal activity we also decided to compare patterns month-by-month - for example, to compare June 2019 (pre-COVID) to June 2020 (post-COVID).  

There are several confounding factors and limitations.  First, we don't know how the rider adjusted all aspects of their behavior to reduce risk - e.g., mask wear and diversion away from crowded trails to city streets. Anecdotally, mask wear was not common in DC during outdoor exercise particularly in the summer.  Secondly, Capital Bikeshare made free memberships available to essential workers during 2020, an additional source of demand with unknown time-of-day and day-of-week patterns.




XXXX 



Raw data had ~48K unique lat  / longs in March 2021 alone…but only 600 stations. Solutions:  
Clean lat/long by taking average per station. 
Reduce lat/long to a small table of about 600 unique values vice 5M+ records. 
Use GEOPY to reverse-code lat-long to get State, County, etc.
Merge new geographic vars into larger file. 



## Key results

REQUIRED: Results: Display and discuss the results. Describe what you have learned and mention the relevance/significance of the results you have obtained.

#### *Bike sharing usage us down during COVID-19*
It is not surprising, that bike sharing fell throughout 2020 due to COVID-19. As infections picked up and lockdowns were announced, bike sharing dropped off and failed to pick up to the pre-COVID levels even by the end of 2020. It is notable that data suggests that people began taking precautions even before official lockdowns were introduced. 

![image](https://user-images.githubusercontent.com/70774260/117549581-37113180-b009-11eb-8da3-1cbdb78c3b52.png)

#### *Bike sharing during commuting hours is sharply down*
Trips for 2020 as a whole shifted from commuting hours to what seems to be leisure hours (afternoons and evenings). However, the change did not occur immediately. Trips were down throughout the day in March 2020 compared to March 2019.  However, there were still a lot of trips during commuting hours. By June, commuting hour trips were much lower than in 2019 and late afternoon trips were up. The finding seems to suggest that after the lockdowns in April, more people might have settled into working from home, but continued to use bike share, this time for leisure

![image](https://user-images.githubusercontent.com/70774260/117549626-7b043680-b009-11eb-9f79-b39dab864536.png)

#### *Weekend trips are up* 
The shift towards bike sharing for leisure away from commuting is also confirmed by our results by day of the week. While total number of trips is still well below pre-COVID-19 levels, the share of weekend trips has picked up meaningfully. In March 2020 trips were way down every day of the week. By June, there were ~500 more weekend trips than in 2019. Finally, by 2021, Saturday trips appear to have fully caught up with pre-COVID-19 levels. 

![image](https://user-images.githubusercontent.com/70774260/117549786-5197da80-b00a-11eb-9d30-f5e559121ef0.png)

#### *Duration of trips has increased*  
People take longer bike rides suggesting that they are riding bikes more for leisure or extended personal use rather than commuting to or from work. 

![image](https://user-images.githubusercontent.com/70774260/117549978-89535200-b00b-11eb-9782-f3e3658bb504.png)

#### *Most frequently used stations are near parks*  
People use stations that are near parks or recreational areas. Top 20 most used stations have changed markedly after the start of the pandemic. This can be particularly useful for health care officials to decide where to dedicate resources of information campaigns on COVID-19 safety (for example posters) or safety equipment as it is not possible, neither cost effective to place these quickly in all possible bike sharing locations. 

The popular rental sites, Gravelly Point and Roosevelt Island are on the Mount Vernon Trail, a narrow path on which maintaining 6 foot social distancing is not possible.  Side routes and adjacent trails are also very narrow. Together, our data suggests a need for increased public health precautions governing outdoor recreational sites during popular leisure hours, especially given bikesharing was even higher on weekends during the pandemic than during the prior year.

![image](https://user-images.githubusercontent.com/70774260/117550102-5cec0580-b00c-11eb-8e40-51a5b32499e6.png)


## Testing of our program 

REQUIRED: Testing: Describe what testing you did. Describe the unit tests that you wrote. Show a sample run of 1 or 2 of your tests (screen captures or copy-and-paste is fine).

We use method-based unit testing for our data cleaning part as well as the data analysis part. We are incorporating our testing into our Jupiter notebook code. We focused mostly on assert tests that our data transformation and aggregation in the process of cleaning and preparing the dataset produces the expected results in the final clean dataset. Below are a few examples of the tests we performed. 
* We checked that our lat/long information is correctly matched to stations where it was missing (earlier part of the data sample). 
* We recalculated the duration of the trip and made sure it is correctly reflected in our dataset. 
* We used assert statements to make sure the groupby split-apply-combine result was as intended.   

![image](https://user-images.githubusercontent.com/70774260/117549451-755a2100-b008-11eb-8d02-80fb248964ce.png)


## Conclusions

We used high frequency information on bike sharing before and after the onset of COVID-19 in DC metropolitan area, focusing on VA specifically. We found that the overall usage of bike sharing has dropped off significantly as the rate of infections picked up. It appears that the use began to fall off already in February, even before the official lockdowns, possibly as people began taking precautions ahead of the official announcements.    

However, after the Virginia's complete lockdown ended in early May, bike sharing continued its seasonal increase even as deaths and hospitalizations escalated, and surpassed the previous year during non-commuting hours and on weekends.  People took longer trips and trips originating from recreational areas also picked up.  Based on this pattern, we concluded that leisure oriented trips increased and substituted for work-related rentals.

Public health care officials and urban planners could use our findings to disseminate information on precautions of using shared resources outdoors during COVID-19. By monitoring frequency of trips during certain days or hours of the day, they can adjust road closures, particularly on the weekends, to relieve bike congestion on crowded paths where social distancing is difficult if not impossible. They could also use this information to place awareness information at the stations that are most frequently used and adjust it accordingly as people return to work and commuting biking begins to return. 

![image](https://user-images.githubusercontent.com/70774260/117548484-442b2200-b003-11eb-8f06-c2fb24eadbf0.png)

In our future work we would like to improve mapping functionality, where we can see on a map the most frequently used stations during different times of day or hour. This way it will be easier for public sector government officials to assess when and where to dedicate more resources to bike sharing and public education campaigns on risks using shared resources outdoors during COVID-19. In addition, we would like to study how essential workers took advantage of Capital Bikeshare's free membership program, first to assess the potential impact of the program and also to separate those trips from what appear to be leisure trips that we see in our data.  

## References

In addition to CS5010 class resources we used the following references:

Chicago Metropolitan Agency for Planning (CMAP), "Pandemic presents opportunity for communities to embrace biking and walking," website post, undated).https://www.cmap.illinois.gov/updates/all/-/asset_publisher/UIMfSLnFfMB6/content/pandemic-presents-opportunity

Kapp, Amy, "Here’s the Latest Expert Guidance on Outdoor Activity and COVID-19," Rails to Trails Conservancy blog post, April 18, 2020, https://www.railstotrails.org/trailblog/2020/april/18/here-s-the-latest-expert-guidance-on-outdoor-activity-and-covid-19/

Dunbar, Harry, "How to Avoid Crowded Trails During COVID-19", BikeArlington blog post, April 24, 2020. https://www.bikearlington.com/how-to-avoid-crowded-trails-during-covid-19/

Data license agreement.  https://www.capitalbikeshare.com/data-license-agreement

Commonwealth of Virginia, "Virginia Open Data Portal:  VDH-COVID-19-PublicUseDataset-Cases", website, https://data.virginia.gov/Government/VDH-COVID-19-PublicUseDataset-Cases/bre9-aqqr

https://dtkaplan.github.io/DataComputingEbook/index.html#table-of-contents

https://towardsdatascience.com/visualizing-bike-mobility-in-london-using-interactive-maps-for-absolute-beginners-3b9f55ccb59

https://towardsdatascience.com/exploring-bike-share-data-3e3b2f28760c

https://towardsdatascience.com/applied-exploratory-data-analysis-the-power-of-visualization-bike-sharing-python-c5b2645c3595


