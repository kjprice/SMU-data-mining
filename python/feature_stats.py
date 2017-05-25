# TODO: replace with full file

housing_raw_a = pd.read_csv('data/ss13husa.csv')
housing_raw_b = pd.read_csv('data/ss13husb.csv')

housing_raw = pd.concat([housing_raw_a, housing_raw_b])

housing_full = housing_raw.copy(deep=True)

#only take numeric columns for analysis
housing_full = housing_full.select_dtypes(include=[np.number])
#optionally limit columnns
#housing_full = housing_full[housing_full.columns[10:16]]


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
   
      data[column] = pd.Series(d, index=i, dtype='int64')
   return pd.DataFrame(data)

df_stats = specialfeatures()

a = df_stats.ACCESS.unique()

print(df_stats)
print('features with the most nulls')
print(df_stats.loc['null_count'].sort_values(ascending=False).head())
print(len(housing_full))

df_stats.transpose().to_csv('./data/stats.csv')