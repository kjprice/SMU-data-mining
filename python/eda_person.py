from pandas.tools.plotting import scatter_matrix
import matplotlib.pyplot as plt

# QOI: Any features that seem to determine income (PINCP)?

# Univariate plots

### Barplot: income
df.PINCP.plot.box(figsize=(10,12))

scatter_matrix(df[dollarFeatures], figsize=(25, 20))


