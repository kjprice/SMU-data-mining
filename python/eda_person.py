from pandas.tools.plotting import scatter_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# QOI: Any features that seem to determine income (PINCP)?

# Univariate plots

### Boxplot: income
df.PINCP.plot.box(figsize=(10,12))
### Boxplot: income (capped at $150,000) (TODO: come up with a better barplot - this is inaccurate)
df_small_income.PINCP.plot.box(figsize=(10,12))

### Histogram: income
plt.xlabel('Income')
df.PINCP.plot.hist(bins=100)
### Histogram: log(income) - not normal but less terrible
df.PINCP.hist(log=True, bins=100)
### Histogram: income - cap at $150K
df_small_income.PINCP.hist(bins=100)

### Histogram of person's age
df.AGEP.hist(bins=40)

### Histogram of income-poverty-ration
df.POVPIP.hist(bins=50)

### StackedBarplot of income response (19% response)
response = pd.crosstab([df.dummy], df.FPINCP.astype(bool))
response.div(response.sum(1).astype(float), axis=0).plot(kind='bar', stacked=True)
# Bivariate Plots

### Scatterplot of all dollar features (TODO: get down to maybe 4 or less)
scatter_matrix(df[important_continuous_features], figsize=(12,10))

### Scatterplot of Income and commute time
df.plot.scatter(x='JWMNP', y='PINCP')

### Scatterplot of Income and Person's Weight  
df.plot.scatter(x='PWGTP', y='PINCP')

### Scatterplot of Income and Citizenship
df.plot.scatter(x='CIT', y='PINCP')
plt.xlabel('Citizenship')
plt.ylabel('Income')
### Boxplot of Income and Citizenship
df.boxplot(column='PINCP', by='CIT')
### ViolinPlot of Income and Citizenship
sns.violinplot(x="CIT", y="PINCP", data=df) # TODO: Add Legend
sns.violinplot(x="CIT", y="PINCP", data=df_small_income) # TODO: Add Legend

### Scatterplot: Person has child?
df.plot.scatter(x='OC', y='PINCP')

### Scatterplot: Income versus age
df.plot.scatter(x='AGEP', y='PINCP')

### Barplot of Income and Ability to speak English (1=Great, 4=Terrible) - No real information - lok at boxplot instead
df.groupby('ENG').PINCP.sum().plot.bar()

### Boxplot of Income by Ability to speak English
df.boxplot(column=['PINCP'], by='ENG')
plt.xlabel('Rating of ability to speak English')
plt.ylabel('Income')

a = df.ENG.astype('category')

