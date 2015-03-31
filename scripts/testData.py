## 03/19/2015
## test program
import csv as csv
import numpy as np
import ipdb
import pandas as pd
import re
#import pylab as P

df = pd.read_csv("../csv/survey.csv", header=0) 

# Calc 1: returns 1
# Calc 2: returns 2
# Linear Algebra or (Vector) Calc III: returns 3
# Upper division math:4 
pCalc1 = re.compile("calc\s+1$")
pCalc2 = re.compile(".*?\calc\s+2$")
pCalc3 = re.compile(".*?\calc\s+3$")
pVCalc3 = re.compile(".*calc$")
pLinearAlgebra = re.compile(".*?\linear\s+algebra$")

#returns the correct number
def math(s):
  s = s.lower()
  if (pCalc1.match(s)):
    return 1
  elif (pCalc2.match(s)): 
    return 2 
  elif (pCalc3.match(s) or pLinearAlgebra.match(s)): 
    return 3
  elif (pVCalc3.match(s)): ##yeah not idea, but does the trick with matching anything ending in 'calc'
    return 3
  else: 
    return 4


    
df["gender"]= df['What is your gender?'].map(lambda u: 1 if u=="Female" else 0)
df["math"] = df['What is the highest level of math that you have taken?'] \
             .map(lambda u: math(u))


df_girls = df[df.gender ==1]
df_boys = df[df.gender ==0]


patternCs51 = re.compile('CS 51$')
df['intro_class'] = df['What CS course(s) are your currently taking?'] \
                    .map(lambda u: 1 if (patternCs51.match(u)) else 0) 


df_51_only = df[df.first_class ==1]
df_51 = pd.concat([df_51_only.gender, df_51_only['How many hours a week do you spend working on CS outside of class and lab?']], axis=1)


df_51_girls = df_51[df_51.gender==1]
df_51_boys = df_51[df_51.gender ==0]


