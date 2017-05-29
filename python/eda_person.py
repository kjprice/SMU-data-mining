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
### Histogram: income - cap at $20K
df[df.PINCP < 20000].PINCP.hist(bins=50)

### Histogram of person's age
df.AGEP.hist(bins=40)

### Histogram of income-poverty-ration
df.POVPIP.hist(bins=50)

### Histogram of commute time
df.JWMNP.hist(bins=len(df.JWMNP.unique()))

### Find weird, large groupings of commute time
df.JWMNP[df.JWMNP.notnull()].astype('int64').value_counts().sort_values().tail().plot(kind='bar')


### StackedBarplot of income response (19% response)
response = pd.crosstab([df.dummy], df.FPINCP.astype(bool))
response.div(response.sum(1).astype(float), axis=0).plot(kind='bar', stacked=True)
# Bivariate Plots

### Scatterplot of all dollar features (TODO: get down to maybe 4 or less)
scatter_matrix(df[important_continuous_features], figsize=(12,10))

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
sns.violinplot(x="CIT_CAT", y="PINCP", data=df) 
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

### Multi-faceted plotting.  commute transportation with time for commuting and total income (Need to create legend)
sns.set(style="ticks")

df_travel = pd.DataFrame(np.c_[df.PINCP, df.JWMNP, df.JWTR],
                  columns=["PINCP", "JWMNP", "JWTR"])
grid = sns.FacetGrid(df, col="JWTR", hue="JWTR", col_wrap=4)
grid.map(plt.axhline, y=0, ls=":", c=".5")
grid.map(plt.plot, "JWMNP", "PINCP", marker="o", ms=4)
grid.fig.tight_layout(w_pad=1)
### Change from numeric to categorical (ordinal)





### Simple plot of years of education and total income
%matplotlib inline
plt.plot(df.SCHL, df.PINCP)  
plt.xlabel('Years of Education')
plt.ylabel('Income')

### Need to eliminate all this since children have been removed from the data ####
### Summary statistics of age of responses with income poverty ratio less than 200 (Determine the right # for the poverty)
## Excluding children
df_adult = df[df.AGEP > 18]
adult_pov = df_adult.AGEP[df_adult.POVPIP<200]
adult_pov.describe()
## Including children
all_pov = df.AGEP[df.POVPIP<200]
all_pov.describe()
## Only Children
df_child = df[df.AGEP <= 18]
pov_child = df_child.AGEP[df_child.POVPIP<200]
pov_child.describe()

### Plot Income and poverty ratio
plt.plot(df.POVPIP, df.PINCP)  
plt.xlabel('Income to Poverty Ratio')
plt.ylabel('Income')

### Create dataframe of only individuals considered in poverty
df_poverty = df[df.POVPIP <100]
plt.plot(df_poverty.POVPIP, df_poverty.PINCP)  
plt.xlabel('Income to Poverty Ratio')
plt.ylabel('Income')

### Confirm negative income values are business owners
df_NegativeInc = df[df.PINCP <0]
df_NegativeInc.COW.value_counts().plot(kind='barh')




# Misc

### Apparently, when the flag for a variables equals 0, there still might be a value for the referenced attribute
df[df.FPINCP == 0].PINCP.head()

### Count number of non-null observations for each feature
### ALL non-null except: POVPIP: 96% && JWMNP 54%
df[important_features].info()



