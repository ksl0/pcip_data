## 03/26/2015
## script to merge datasets and add a few columns
import csv as csv
import numpy as np
import ipdb
import pandas as pd
import sexmachine.detector as gender
#import pylab as P
# get the gender correlator
d = gender.Detector(case_sensitive=False)
## read in the spreadsheet
xl = pd.ExcelFile('../csv/Combined_NC.xls')
df = xl.parse(sheetname="Combined_NC")


## only are interested in variables: 
# age, political affilation, gender    

binaryGenderFunction = lambda  u: 1 if (u=="mostly_female" or u =="female") else 0
ageAppropriateMarriage = lambda age1, age2: 1 if (age1 > 16 and age2 > 16 and abs(age1 - age2) < 15) else 0
# apologies for the simplified model, will look to use longer term data to define strength of relationship asap 
heterosexualViewOfTheWorld = lambda bG1, bG2: 0 if (bG1 == bG2) else 1 # inaccurate, non-inclusive  gender assumptions
assumedJuvenileChild = lambda u: 1 if (u < 19) else 0

df['gender_predicted'] = df.name_first.map(lambda u: d.get_gender(u))
df["gender2"]= df.gender_predicted.map(binaryGenderFunction)
df_ugh = df[df["address", "name_first", "name_last", "gender2", "age","party"]]

##TODO: add a for loop to make combinations of each item in the potential grouped by   
# Goal: spit out number of children, 
# currently f doesn't do anything, but should do something interesting soon

f = lambda u: u

df_ugh.groupBy(['address']).map(f)




