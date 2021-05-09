# CS5010 Final Project

Jenny Jang, 
Carol Moore, 
Elina Ribakova 

Github repository: https://github.com/Eribakova/CS5010

Relevant Juyter Notebooks:  Datacleaning_Final.ipynb and Analysis_Final.ipynb

Link to Google Drive with all the Datasets mentioned in the report: https://drive.google.com/drive/folders/1af62oMJvt0VrC8fkSnE-8pq36EJRhDcc?usp=sharing

## Bike-Sharing: Insight into Public Precautions During the COVID-19 Pandemic

<img src="https://github.com/Eribakova/CS5010/blob/main/Bike.PNG">

## Objectives

This project explores how outdoor activity changed with COVID-19, which a focus on bikesharing.  In the Washington DC area, there were mixed policies about outdoor social gatherings.  Many parks were closed throughout the summer. However, recreational pathways remained open even where social distancing was difficult if not impossible, and the major DC area trails remained crowded and even broke weekend records for usage in March 2020 as cases were escalating. We examined the public's use of rental bikes to gauge how the public took precautions or increased their risks throughout 2020 to the present. 

Our central analytic question is whether bikesharing declined in Virginia relative to the previous year. Many cities reported a spike in bicycle sales and bike sharing. For example, Chicago reported “unprecedented demand” in its bike-sharing system.  We wanted to see if the Washington DC area experienced a similar spike or if public health restrictions and precautions - which reduced tourism and commuting -- caused a net reduction in usage, mitigating the potential risks of biking on narrow paths and on roads.  If the public were consistently taking increased precautions in all aspects of their public behavior we would expect to see bikesharing decrease and for trips to be shorter, especially in more crowded areas.  

Finally, we hoped to explore how an analysis like this, if expanded, could be used in urban planning, transportation, and public health policies.  Briefly, we conclude that our analysis could help tailor the pandemic response regarding bikesharing and other forms of outdoor recreation.

Our Github repository located at is Eribakova/CS5010.  Our data files, which were too large to load up to Github, are located at 

## Data set

We used Capital Bikeshare’s Trip History dataset which is licensed for public use by Motivate, the company that operates Capital Bike share on behalf of Washington, DC area municipalities.  Capital Bikeshare maintains over 4,300 bikes across DC, Maryland and Northern Virginia and is the dominant bike sharing company in the region.  The data are available at https://www.capitalbikeshare.com/system-data. 

We downloaded 25 monthly data files from February 2019 to March 2021, the most recent file available.  Each record is a trip from a starting kiosk, or station, to an end station.  Data fields include starting and ending station address, a date-timestamp (year-month-day-hour-minute-second) and the type of renter, e.g., casual or membership.  In the most recent part of the dataset, longitude and latitude data for bike stations was also provided. 

Public health data provided helpful context for understanding bikesharing trends. We obtained epidemiological data from https://data.virginia.gov/Government/VDH-COVID-19-PublicUseDataset-Cases/bre9-aqqr. The dataset provided information on hospitalizations and mortality rates by locale in Virginia. These data were merged in with the bikeshare data to complete our file.

## Data Pipeline

The Python code for preprocessing and cleaning is in the file Datacleaning_Final.ipynb.

### Preprocessing

In order to concatenate the 25 monthly bike share files into a single data set, we assessed if there were inconsistencies in the structure of the files over time.  We found that column headings and formats differed for files before and after May 2020. In most cases, however, the file format differences were not significant.  We ran each monthly dataframe through a for-loop to standardize headings, which allowed the files to be concatenated, resulting in a file of over 5.5M records. Once we standardized our data, we merged in daily COVID case counts by matching dates. 

#### Figure 1.  Standardizing column headings
![image](https://user-images.githubusercontent.com/70774260/117550168-ccfa8b80-b00c-11eb-9731-bbc6930c5a46.png)

#### Figure 2.  Merging Public Health Data
![image](https://user-images.githubusercontent.com/70774260/117550185-ed2a4a80-b00c-11eb-85e2-c14fe658900e.png)

### Cleaning

The merged dataset included numerous irregularities and missing values that had to be remedied prior to analysis. We eliminated trips with outlying durations spanning multiple days, where likely someone did not return a bike).  The data set had street address information but lacked city and state, aggregates that we believed would be more closely tied to public health regulations and that would be more tractable to work with.  

#### Figure 3.  Raw address data
![image](https://user-images.githubusercontent.com/70774260/117550233-38445d80-b00d-11eb-8a8e-e16fbdd0184d.png)

We used the Python GEOPY library to extract city and state from the latitude and longitude.  There were several issues which we solved in the following ways.

1.  Lat/long data were missing from all files dated prior to May 2020.  We created a dictionary to map lat/long to each station where data was available, then used the dictionary to fill in lat/long based on station id. Because the stations did not change much, if at all, during our timeframe, this was possible. 

2.  Lat/long data were not standard, differing greatly in the number of decimal places.  This resulted, for example, in over 48,000 unique lat/longs for fewer than 600 stations in the March 2021 file alone. As a result, and because we were trying to run GEOPY over every observation in the file, the reverse gecode runtime totaled over 3 hours for one month's data.  Our solution was to take the mean lat-long grouped by station id and run GEOPY over a small table that listed each station with its average lat/long.  Having cleaned and reduced the data, we easily extracted State and city information.  The breakdown of state is shown below:

District of Columbia:  4,892,84
Virginia:  590,687
Maryland: 135,035
NaN: 119,252

Based on this information we decided to limit the project Virginia only, so that the final dataset consists of 590,687 bikesharing trips that started in Northern Virginia.

## Experimental Design

Our approach was to compare bike sharing patterns 'pre-COVID' and 'post-COVID'.  Because bicycling is a seasonal activity we also decided to compare patterns month-by-month - for example, to compare June 2019 (pre-COVID) to June 2020 (post-COVID).  

There are several analytic limitations.  First, we don't know how the rider adjusted all aspects of their behavior to reduce risk - e.g., mask wear and diversion away from crowded trails to city streets. Anecdotally, mask wear was not common in DC during outdoor exercise particularly in the summer.  Secondly, Capital Bikeshare made free memberships available to essential workers during 2020, an additional source of demand with unknown implications for overall trip count and patterns of use. Finally, there were no bikeshares in April 2020 during the lockdown and as a result our dataset lacks any data for April.  

We planned four main queries:
1.  How did the number of monthly trips change in 2020 compared to 2019?
2.  Did the amount of time spent riding change?
3.  How did time of day and day of week change?  Do the shifts reflect changes in commuting, leisure, or both?
4.  Where did trips change?  Is there a locational pattern to the change?

The analysis and visualization code, along with additional visualizations, is in our Jupyter notebook.  An important coding tool was the Pandas 'groupby' method.  We used groupby to aggregate the data and develop monthly, weekly, daily and hourly counts.  The Seaborn library was also important to our analysis.  Seaborn easily makes bar charts that are useful in 'pre-/post-analysis' because the 'hue' keyword enables dimensions beyond the x and y axis.  This feature allowed us to incorporate "year" into the charts, enabling clear year-to-year comparisons.

## Key results

#### *Bike sharing usage us down during COVID-19*
It is not surprising, that bike sharing fell throughout 2020 due to COVID-19. As infections picked up and lockdowns were announced, bike sharing dropped off and failed to pick up to the pre-COVID levels even by the end of 2020. It is notable that data suggests that people began taking precautions even before official lockdowns were introduced, since trips were lower in February than January 2020. 

#### Figure 4.  COVID-19 events and trip counts compared to 2019
![image](https://user-images.githubusercontent.com/70774260/117549581-37113180-b009-11eb-8da3-1cbdb78c3b52.png)

#### *Bike sharing during commuting hours is sharply down*
Trips for 2020 as a whole shifted from commuting hours to what seems to be leisure hours (afternoons and evenings). However, the change did not occur immediately. Trips were down throughout the day in March 2020 compared to March 2019.  However, there were still a lot of trips during commuting hours. By June, commuting hour trips were much lower than in 2019 and late afternoon trips were up. The finding seems to suggest that after the lockdowns in April, more people might have settled into working from home, but continued to use bike share, this time for leisure.  Our display below shows March and June 2020; visualizations in our Jupyter Notebook confirm the trend continued after June.

#### Figure 5.  Trip count by time of day
![image](https://user-images.githubusercontent.com/70774260/117549626-7b043680-b009-11eb-9f79-b39dab864536.png)

#### *Weekend trips are up* 
The shift towards bike sharing for leisure away from commuting is also confirmed by our results by day of the week. While total number of trips is still well below pre-COVID-19 levels, the share of weekend trips has picked up meaningfully. In March 2020 trips were way down every day of the week. By June, there were ~500 more weekend trips than in 2019. Finally, by 2021, Saturday trips appear to have fully caught up with pre-COVID-19 levels. Our display below shows March and June 2020; visualizations in our Jupyter Notebook confirm the trend continued after June.

#### Figure 6.  Trip count by day of week
![image](https://user-images.githubusercontent.com/70774260/117549786-5197da80-b00a-11eb-9d30-f5e559121ef0.png)

#### *Duration of trips has increased*  
People take longer bike rides suggesting that they are riding bikes more for leisure or extended personal use rather than commuting to or from work. 

#### Figure 7.  Distribution of trip duration, pre- and post-COVID, by time of day
![image](https://user-images.githubusercontent.com/70774260/117549978-89535200-b00b-11eb-9782-f3e3658bb504.png)

#### *Most frequently used stations are near parks*  
People use stations that are near parks or recreational areas. Top 20 most used stations have changed markedly after the start of the pandemic. This can be particularly useful for health care officials to decide where to dedicate resources of information campaigns on COVID-19 safety (for example posters) or safety equipment as it is not possible, neither cost effective to place these quickly in all possible bike sharing locations. 

The popular rental sites, Gravelly Point and Roosevelt Island are on the Mount Vernon Trail, a narrow path on which maintaining 6 foot social distancing is not possible.  Side routes and adjacent trails are also very narrow. Together, our data suggests a need for increased public health precautions governing outdoor recreational sites during popular leisure hours, especially given bikesharing was even higher on weekends during the pandemic than during the prior year.

#### Figure 8.  Ranking of start stations, pre- and post-COVID
![image](https://user-images.githubusercontent.com/70774260/117550102-5cec0580-b00c-11eb-8e40-51a5b32499e6.png)


## Testing of our program 

We use method-based unit testing for our data cleaning part as well as the data analysis part. We are incorporating our testing into our Jupiter notebook code. We focused mostly on assert tests that our data transformation and aggregation in the process of cleaning and preparing the dataset produces the expected results in the final clean dataset. Below are a few examples of the tests we performed. 
* We checked that our lat/long information is correctly matched to stations where it was missing (earlier part of the data sample). 
* We recalculated the duration of the trip and made sure it is correctly reflected in our dataset. 
* We used assert statements to make sure the groupby split-apply-combine result was as intended (note that this approach yields no output if the statement is True).

#Figure 9. Example of testing with Assert statements
![image](https://user-images.githubusercontent.com/70774260/117549451-755a2100-b008-11eb-8d02-80fb248964ce.png)


## Conclusions

We used high frequency information on bike sharing before and after the onset of COVID-19 in DC metropolitan area, focusing on VA specifically. We found that the overall usage of bike sharing has dropped off significantly as the rate of infections picked up. It appears that the use began to fall off already in February, even before the official lockdowns, possibly as people began taking precautions ahead of the official announcements.    

However, after the Virginia's complete lockdown ended in early May, bike sharing continued its seasonal increase even as deaths and hospitalizations escalated, and surpassed the previous year during non-commuting hours and on weekends.  People took longer trips and trips originating from recreational areas also picked up.  Based on this pattern, we concluded that leisure oriented trips increased and substituted for work-related rentals.

Public health officials could use the data to tailor interventions beyond what the vendor is already doing (sanitizing high-contact parts of the equipment after use). These could include posting safety information posters at the bikesharing stations that are most frequently used, requiring a review of social distancing guidelines as part of the terms of the rental, emphasizing the value of mask wear for outdoor recreation, or limiting rentals where social distancing is not possible. 

Urban planners could use this information to assess which roads might be closed on weekends to promote fitness and recreation, to enable more social distancing than is possible on trails.  By monitoring frequency of trips during certain days or hours of the day, they can adjust road closures, particularly on the weekends, to relieve bike congestion on crowded paths where social distancing is difficult if not impossible. 

There are a few technical limitations we would overcome with more time.  For example, rather than simply omitting April 2020, we would treat April 2020 as a month with zero bikeshares, and include public health case data for that month.  Doing so would have enabled a greater variety of charts, such as line charts, showing trends and correlations over time.  Second, we would have explored mapping visualizations.

To increase the utility of this analysis, we would develop a user query interface with mapping functionality, where we can see on a map the most frequently used stations during different times of day or hour. This way it will be easier for public sector government officials to assess when and where to dedicate more resources to bike sharing and public education campaigns on risks using shared resources outdoors during COVID-19. In addition, we would seek additional data on essential workers who took advantage of Capital Bikeshare's free membership program, first to assess the potential impact of the program and also to separate those trips from what appear to be leisure trips.  

Figure 10.  Summary
![image](https://user-images.githubusercontent.com/70774260/117548484-442b2200-b003-11eb-8f06-c2fb24eadbf0.png)


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


