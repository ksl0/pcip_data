## 04/05/2015
## script to merge datasets and add a few columns

import csv as csv
import ipdb
import pandas as pd
import sexmachine.detector as gender
import itertools as iters

#import pylab as P
# get the gender correlator
d = gender.Detector(case_sensitive=False)

## read in the spreadsheet
xl = pd.ExcelFile('../csv/Combined_NC.xls')
df = xl.parse(sheetname="Combined_NC")

##gender file
df['gender_predicted'] = df.name_first.map(lambda u: d.get_gender(u))
getGender = lambda  u: 0 if (u=="mostly_female" or u =="female") else 15

## males get a 15 point greater than females
df["real_age"] = df.apply(lambda u: 0 if (u["Age"] < 19 or u["Age"] > 70) else u["Age"], axis=1)

## assume the array is as follows:
## stOwnerAseeName, name_first, name_last
ownerRank = lambda (own, f, l): 100 if ((f in own) and (l in own)) else 0

df["owner"] = df.apply(lambda x: 100 if x["name_first"] in x["stOwnerAsseeName"] \
                       and x["name_last"] in x["stOwnerAsseeName"] else 0, axis=1)

print "done finding owner"

df["gender2"]= df.gender_predicted.map(getGender)
df_analysis= df[["address","stOwnerAsseeName",  "name_first", "name_last", "gender2", "Age"]]

print "done finding mapping gender"

##ranking algorithm 
df["rank"] = df.apply(lambda u: u["real_age"] +u["gender2"] + u["owner"], axis=1)

print "finished with rank"

result = df.sort(['rank'], ascending=False).groupby(['address']).apply(lambda u: u.head(1))
result[["Age", "gender", "gender2", "rank", "name_last", "name_first", "owner", "stOwnerAsseeName"]].to_csv("initial_result.csv")




