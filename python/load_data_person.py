import pandas as pd
import numpy as np
import sys
import os

print (sys.version)
print (os.getcwd())

person_raw = pd.read_csv('data/person-subset-2.5percent.csv')

#Jen - - some changes to load the data
os.chdir('c:/Users/nizzi/Documents/DataMiningProj/SMU-data-mining/data')
person_raw = pd.read_csv('person-subset-2.5percent.csv')

