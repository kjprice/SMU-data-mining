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

### Histogram of income-poverty-ration
df.POVPIP.hist(bins=50)

### StackedBarplot of income response (19% response)
response = pd.crosstab([df.dummy], df.FPINCP.astype(bool))
response.div(response.sum(1).astype(float), axis=0).plot(kind='bar', stacked=True)
# Bivariate Plots

### Scatterplot of all dollar features (TODO: get down to maybe 4 or less)
scatter_matrix(df[dollarFeatures], figsize=(25, 20))

### Scatterplot of Income and commute time
df.plot.scatter(x='JWMNP', y='PINCP')
plt.xlabel('Commute Time in minutes')
plt.ylabel('Income')


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

### Barplot of Income and Ability to speak English (1=Great, 4=Terrible) - No real information - lok at boxplot instead
df.groupby('ENG').PINCP.sum().plot.bar()

### Boxplot of Income by Ability to speak English
df.boxplot(column=['PINCP'], by='ENG')
plt.xlabel('Rating of ability to speak English')
plt.ylabel('Income')


### Multi-faceted plotting.  commute transportation with time for commuting and total income (Need to create legend)
sns.set(style="ticks")

df_travel = pd.DataFrame(np.c_[df.PINCP, df.JWMNP, df.JWTR],
                  columns=["PINCP", "JWMNP", "JWTR"])
grid = sns.FacetGrid(df, col="JWTR", hue="JWTR", col_wrap=4)
grid.map(plt.axhline, y=0, ls=":", c=".5")
grid.map(plt.plot, "JWMNP", "PINCP", marker="o", ms=4)
grid.fig.tight_layout(w_pad=1)
#           01 .Car, truck, or van
#           02 .Bus or trolley bus
#           03 .Streetcar or trolley car (carro publico in Puerto Rico)
#           04 .Subway or elevated
#           05 .Railroad
#           06 .Ferryboat           
#           07 .Taxicab
#           08 .Motorcycle
#           09 .Bicycle
#           10 .Walked
#           11 .Worked at home
#           12 .Other method





