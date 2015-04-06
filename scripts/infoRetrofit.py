
import csv as csv
import numpy as np
import pandas as pd
import pylab as P
import decimal


## get the retrofit and the voter files
df_retrofit = pd.read_csv("../csv/retrofit.csv", header=0) 
df_vote = pd.read_csv('../csv/vote.csv', header=0) 

## replace the label of the df_vote
## merge the two datasets based on the Address parameter
df_vote = df_vote.rename(columns = {'mail_street':'Address'})
df_fit = pd.merge(df_retrofit, df_vote, how='outer', on='Address')

### keep only cherp data
df = df_fit[df_fit.Name.isnull()==False]

df = pd.read_csv("../csv/retrofit.csv", header=0) 
df_retrofit = df[pd.notnull(df.Address)]

## remove pilgrim place data by replacing the address
## values with nan, and then dropping those from the data
f = lambda x:  np.nan if "pilgrim" in x.lower() else x
df_retrofit['Name']= df_retrofit['Name'].map(f)
## drop again
## occassionally there is an extra comment after the price, so split the string and take the later one
removeComma = lambda x: np.nan if pd.isnull(x) else decimal.Decimal(x.replace(',', '').replace('$','').split()[0])
df_retrofit['Total Cost of Job'] = df_retrofit['Total Cost of Job'].map(removeComma)
df_retrofit['% Reduction (modeled)'] = df_retrofit['% Reduction (modeled)'].map(lambda x : np.nan if pd.isnull(x) else int(x.replace('%', '')))
df_nopilgrim = df_retrofit[pd.notnull(df_retrofit.Name)]



