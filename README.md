# CS5010 Final Project

Jenny Jang
Carol Moore
Elina Ribakova 

## BikeShare Data Analysis comarping pre-covid and post-covid

<img src="github.com/Eribakova/CS5010/blob/main/Bike.PNG">

### Introduction

We wanted to explore some idea on how people's social behavior changed with covid. Our focus is on a change of trend in bikesharing. Here are some example questions we thought to find out:

1. Did the number of trips change from pre-COVID and post-COVID?
2. Did any COVID even change the bikeshare frequency?
3. Comaprison between suburb area and city area.


### Introducing our DATASET

We got our dataset from 'Capital Bikshare', from following webseite: https://www.capitalbikeshare.com/system-data
For our project, we concatenated monthly dataset from Februrary 2019 to Februrary 2021. We then filled out missing values such as 'lat' and 'long' since dataset before covid did that have that information. We then extracted State from lat/long information then decided to use final dataset with records only from 'Virginia'.


### Testing of our program 

We use method-based unit testing for our data cleaning part as well as the data analysis part. We are incorporating our testing into our Jupiter notebook code. We focused mostly on assert tests that our data transformation and aggregation in the process of cleaning and preparing the dataset produces the expected results in the final clean dataset. Below are a few examples of the tests we performed. 
* We checked that our lat/long information is correctly matched to stations where it was missing (earlier part of the data sample). 
* We recalculated the duration of the trip and made sure it is correctly reflected in our dataset. 


