import pandas as pd
import numpy as np
import sys
import os

print (sys.version)
print (os.getcwd())

housing_raw = pd.read_csv('data/housing-subset-5percent.csv')

