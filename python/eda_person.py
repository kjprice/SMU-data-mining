from pandas.tools.plotting import scatter_matrix
import matplotlib.pyplot as plt

# QOI: Any features that seem to determine income (PINCP)?

# Univariate plots

### Boxplot: income
df.PINCP.plot.box(figsize=(10,12))
### Boxplot: income (capped at $150,000) (TODO: come up with a better barplot - this is inaccurate)
df[df.PINCP < 150000].PINCP.plot.box(figsize=(10,12))

scatter_matrix(df[dollarFeatures], figsize=(25, 20))


