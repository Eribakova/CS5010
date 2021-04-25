#!/usr/bin/env python
# coding: utf-8


#Start a log for error reporting

fileout=open("Exception_Log.txt",'a')

#Create County variable
countyls=[]
for i in newlst:
  try:
    location=(geolocator.reverse(i))
    address = location.raw['address']
    county = address.get('county', '')
    countyls.append(county)
  except:
    print('error in',i)
    fileout.write(i)
    break
temp['county']=countyls


# In[ ]:


#Create City variable
cityls=[]
for i in newlst:
  try:
    location=(geolocator.reverse(i))
    address = location.raw['address']
    city = address.get('city', '')
    cityls.append(city)
  except:
    print('error in',i)
    fileout.write(i)

    break
temp['city']=cityls

fileout.close()
# In[ ]:


#This section combines county and city to create a single 'locale' variable.
#https://www.codegrepper.com/code-examples/python/pandas+replace+column+values+with+another+column
temp['locale']=temp['county']
temp['locale'] = np.where(temp['locale'] == "", temp['city'], temp['locale'])

temp

