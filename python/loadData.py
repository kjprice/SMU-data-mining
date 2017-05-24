import sys
print (sys.version)

import os
print (os.getcwd())

import pandas as pd
import numpy as np

housing_a_raw = pd.read_csv('data/ss13husa.csv')
