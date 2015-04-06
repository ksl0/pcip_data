## 03/21/2015
## add variables: 
## 1. gender 2. party affiliation 3. marriage 
## 4. head of the household

import csv as csv
import numpy as np
import ipdb
import pandas as pd
#import pylab as P

## import the needed data, contains all resident data
df_retrofit = pd.read_csv("../csv/retrofit.csv", header=0) 
df_vote = pd.read_csv('../csv/vote.csv', header=0) 

## replace the label of the df_vote
## merge the two datasets based on the Address parameter
df_vote = df_vote.rename(columns = {'mail_street':'Address'})
df_fit = pd.merge(df_retrofit, df_vote, how='outer', on='Address')

### keep only cherp data
df_cherp_only = df_fit[df_fit.Name.isnull()==False]

## add columns in occupants, republicans, democrats, other, 
## 1 indicated in the party, otherwise they are not
df_cherp_only["DEM"]= df_cherp_only.party.map(lambda u: 1 if u=="DEM" else 0)
df_cherp_only["REP"]= df_cherp_only.party.map(lambda u: 1 if u=="REP" else 0)

## find the size of the household
##address = df_cherp_only.groupby(['Name'])['Address'].apply(lambda u: u) # do nothing to addresss
house = df_cherp_only.groupby(['Name']).size()
dem = df_cherp_only.groupby(['Name'])['DEM'].sum()
rep = df_cherp_only.groupby(['Name'])['REP'].sum()

listOutput = [house, dem, rep] 
result = pd.concat(listOutput, axis=1)

result.to_csv('../csv/politics.csv')
"""
writer = pd.ExcelWriter('output.xlsx')
result.to_excel(writer, 'Data_Analytics')
writer.save() """ 
## TODO import some stuff, reformate the mapping of the dataframe >.<

