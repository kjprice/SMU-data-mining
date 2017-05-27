import pandas as pd
import numpy as np
import sys
import os

print (sys.version)
print (os.getcwd())

housing_raw = pd.read_csv('data/housing-subset-5percent.csv')


#Jen - - some changes to load the data
os.chdir('c:/Users/nizzi/Documents/DataMiningProj/SMU-data-mining/data')
housing_raw = pd.read_csv('housing-subset-5percent.csv')
