import pandas as pd
import numpy as pd
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(13,14))
fig.savefig('fig1.png', dpi = 300)


df.info()

# Group by Telephone
df.TEL.value_counts().plot(kind='bar')

# Gross Rent
df[df.FGRNTP == 1.0].GRNTP.hist()

# Number of related children in household
df.NRC.hist() 

# Number of own children in household
df.NOC.hist()

# Number of persons in family
df.NPF.hist()

# Houselhold income
df.HINCP.plot.box()
df[df.HINCP < 200000].HINCP.plot.box()




# try to get an accurate representation of poverty