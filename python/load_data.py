import pandas as pd
import numpy as np
import sys
import os

print (sys.version)
print (os.getcwd())

os.chdir('/Users/kjprice/Library/Projects/smu/data-mining/Data Mining Project/')

housing_raw = pd.read_csv('data/housing-subset-5percent.csv')




#Jen - - some changes to load the data
housing_raw = pd.read_csv('housing-subset-5percent.csv')
