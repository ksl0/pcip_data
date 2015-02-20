# 01/14/2014
# A combination of notes and code from the python tutorial
# UC4P - 'uncomment for plot'
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
    singularAddress = []
    data = req.get(url).json()
    return singularAddress 

#needs to have an address column in df
def populate_claremont_address(dataFrame): 
    lat = [] 
    lon = [] 
    address_formed = [] 
    
    for i in dataFrame.Address: 
        if (math.isnan(i)):
           lat.append(np.nan) 
           lon.append(np.nan) 
           address_formed(np.nan)
        else:
           lat.append(
           
    
	      

#if __name__=="__main__":

df['url'] = df.Address.map(lambda x: format_address(base_url, x, bounds))
df['lat'] = np.nan
df['lon'] = np.nan
df['address_formatted'] = np.nan


