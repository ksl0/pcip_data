## 03/26/2015
## script to merge datasets and add a few columns
## extremely specific to the datatype: but get stuff done

import csv as csv
import numpy as np
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

print "done parsing"
## only are interested in variables: 
# age, political affilation, gender    

binaryGenderFunction = lambda  u: 1 if (u=="mostly_female" or u =="female") else 0

ageAppropriateMarriage = lambda u: 1 if (u[1][1][4] > 16 and u[0][1][4] > 16 and abs(u[0][1][4] - u[1][1][4]) < 15) else 0


isHetero = lambda u: 0 if (u[0][1][3]== u[1][1][3]) else 1 # inaccurate, non-inclusive  gender assumptionsh

assumedJuvenileChild = lambda u: 1 if (u < 19) else 0

df['gender_predicted'] = df.name_first.map(lambda u: d.get_gender(u))
df["gender2"]= df.gender_predicted.map(binaryGenderFunction)
df_analysis= df[["address", "name_first", "name_last", "gender2", "Age","party"]]

##TODO: add a for loop to make combinations of each item in the potential grouped by   
# Goal: spit out number of children, 
# currently f doesn't do anything, but should do something interesting soon

f = lambda u: map(lambda pair: isHetero(pair)==1,list(iters.combinations(u.iterrows(),2)))[0]



 ## 1 if True in map(lambda u: list(iters.combinations(df_analysisiterrws(),2))

df_analysis.groupby(['address']).apply(f)


