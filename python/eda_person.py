from pandas.tools.plotting import scatter_matrix
import matplotlib.pyplot as plt

# QOI: Any features that seem to determine income (PINCP)?

# Univariate plots

### Boxplot: income
df.PINCP.plot.box(figsize=(10,12))
### Boxplot: income (capped at $150,000) (TODO: come up with a better barplot - this is inaccurate)
df[df.PINCP < 150000].PINCP.plot.box(figsize=(10,12))

### Histogram: income
df.PINCP.plot.hist(bins=100)
### Histogram: log(income) - not normal but less terrible
df.PINCP.hist(log=True, bins=100)
### Histogram: income - cap at $150K
df[df.PINCP < 150000].PINCP.hist(bins=100)

### StackedBarplot of income response (19% response)
response = pd.crosstab([df.dummy], df.FPINCP.astype(bool))
response.div(response.sum(1).astype(float), axis=0).plot(kind='bar', stacked=True)
# Bivariate Plots

### Scatterplot of all dollar features (TODO: get down to maybe 4 or less)
scatter_matrix(df[dollarFeatures], figsize=(25, 20))

### Scatterplot of Income and commute time
df.plot.scatter(x='JWMNP', y='PINCP')

### Scatterplot of Income and Person's Weight
df.plot.scatter(x='PWGTP', y='PINCP')

### Barplot of Income and Ability to speak English (1=Great, 4=Terrible) - No real information - lok at boxplot instead
a = df.groupby('ENG').PINCP.sum().plot.bar()

### Boxplot of Income by Ability to speak English
df.boxplot(column=['PINCP'], by='ENG')

