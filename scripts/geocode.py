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
# ipdb.set_trace()

df = pd.read_csv('../csv/retrofit.csv', header=0)
base_url ='https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}&bounds={2}'
key = keys.API_KEY

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
    a = "+".join(address.split())
    formatted = base_url.format(a, key, bound)
  return formatted 

##returns a list with latitude, longitute, and the address
def get_data(url): 
    print url
    data = req.get(url).json()
    dictionary = {}
    adrs = data['results'][0]['formatted_address'].encode()
    lat = data['results'][0]['geometry']['location']['lat'] 
    lng = data['results'][0]['geometry']['location']['lng'] 
    dictionary = {'address_f': [adrs], 'lat': [lat], 'lng': [lng]} 
    return dictionary 

#needs to have an address column in df
#returns the series object

dct = {}
def populate_claremont_address(dataFrame, bounds): 
    dct['lat'] = [] 
    dct['lng'] = []
    dct['address_f'] = []
    for i in dataFrame.Address: 
        if (pd.isnull(i)):
           dct['lat'].append(np.nan) 
           dct['lng'].append(np.nan) 
           dct['address_f'].append(np.nan)
        else:
    	   url = format_address(base_url, i, bounds)
           print url
           nDict = get_data(url)
           dct['lat'].append(nDict["lat"][0]) 
           dct['lng'].append(nDict["lng"][0])
           dct['address_f'].append(nDict["address_f"][0])
           

#if __name__=="__main__":

bounds =  claremontCityLimits();
df['url'] = df.Address.map(lambda x: format_address(base_url, x, bounds))

#df.append(s, ignore_index=True)

#test dataframe


testDF = pd.DataFrame(df.Address[0:3])
