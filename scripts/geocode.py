# 01/14/2014
# A combination of notes and code from the python tutorial
# UC4P - 'uncomment for plot'
#TODO add a catch for when the address does not return results

import csv as csv
import numpy as np
import ipdb
import pandas as pd
#import pylab as P
import requests as req
import json
import keys
import time
import math
# the debugger
#ipdb.set_trace()
df = pd.read_csv('../csv/retrofit.csv', header=0)
#df = df[2:3]
base_url ='https://maps.googleapis.com/maps/api/geocode/json?address={0}&bounds={2}&key={1}'
key = keys.API_KEY
city = "claremont"
newDF = pd.DataFrame();
testing = {}

# from http://www.maptechnica.com/us-city-boundary-map/city/Claremont/state/CA/cityid/0613756
def claremontCityLimits(): 
  NorthBound = 34.165396
  SouthBound = 34.079477
  EastBound = -117.750793
  WestBound = -117.677576
  bound = str(NorthBound) +"," + str(WestBound) + "|" + str(SouthBound) + "," + str(EastBound)
  return bound

def format_address(base_url, address, bound): 
  if (pd.isnull(address)): 
    formatted = np.nan
  else: 
    atemp = (address.split())
    atemp.append(city)
    a = "+".join(atemp)
    formatted = base_url.format(a, key, bound)
  return formatted 

##returns a list with latitude, longitute, and the address
bad_urls = {}
def get_data(url): 
    data = req.get(url).json()
    testing.update(data)
    dictionary = {}
    print data
    if (len(data['results']) == 0): 
       adrs = np.nan
       lat = np.nan
       lng = np.nan
       place_id = np.nan
       bad_urls["url"] = [url]
    else: 
      adrs = data['results'][0]['formatted_address'].encode('ascii', 'ignore')
      lat = data['results'][0]['geometry']['location']['lat'] 
      lng = data['results'][0]['geometry']['location']['lng'] 
      place_id = data['results'][0]['place_id'].encode()
    dictionary = {'place_id': [place_id], 'address_f': [adrs], 'lat': [lat], 'lng': [lng]} 
    return dictionary 

#needs to have an address column in df
#returns the series object

def populate_claremont_address(dataFrame, bounds): 
    dct = {}
    dct['lat'] = [] 
    dct['lng'] = []
    dct['address_f'] = []
    dct['place_id'] = []
    for i in dataFrame.Address: 
        print i
        time.sleep(0.2) #make sure not to exceed API limits
        if (pd.isnull(i)):
           dct['lat'].append(np.nan) 
           dct['lng'].append(np.nan) 
           dct['address_f'].append(np.nan)
           dct['place_id'].append(np.nan)
        else:
    	   url = format_address(base_url, i, bounds)
           nDict = get_data(url)
           dct['lat'].append(nDict["lat"][0]) 
           dct['lng'].append(nDict["lng"][0])
           dct['address_f'].append(nDict["address_f"][0])
           dct['place_id'].append(nDict["place_id"][0])
    return dct 
           

if __name__=="__main__":
  bounds =  claremontCityLimits();
  df['url'] = df.Address.map(lambda x: format_address(base_url, x, bounds))

  dct = populate_claremont_address(df, bounds)
  newDF =pd.DataFrame(dct) 
  #make sure the urls are private
  df = df.drop('url', 1)  
  notes = pd.DataFrame(bad_urls)
  results = pd.concat([df, newDF] , axis =1)
  results.to_csv('../csv/out.csv')
  notes.to_csv('../csv/notes.csv')


