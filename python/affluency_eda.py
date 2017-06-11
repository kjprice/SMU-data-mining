import matplotlib.pyplot as plt

### Create two histograms - one for each category - this is cmpletely wrong for some reason
df.groupby('affluency').PINCP.hist(bins=100)

### Show bar chart comparing frequency of two categories
df.affluency.value_counts().plot(kind='bar')
plt.show()
