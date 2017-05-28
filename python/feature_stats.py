# TODO: replace with full file
import pandas as pd
import numpy as np


housing_full = df.select_dtypes(include=[np.number])


def specialfeatures():
   data = {}
   for column in housing_full:
      if column[0:4] == 'wgtp':
         continue
      feature = housing_full[column]
      d = []
      i = []
   
      i.append('max_value')
      d.append(np.max(feature))
   
      i.append('null_count')
      d.append(np.sum(feature.isnull()))
      
      i.append('unique_values')
      d.append(int(len(feature.unique())))

      if not np.isnan(d[0]):
        data[column] = pd.Series(d, index=i, dtype='int64')
   return pd.DataFrame(data)

df_stats = specialfeatures()

df_stats.transpose().to_csv('./data/stats-person-subset.csv')

print(df_stats)
print('features with the most nulls')
print(df_stats.loc['null_count'].sort_values(ascending=False).head())
print(len(housing_full))
