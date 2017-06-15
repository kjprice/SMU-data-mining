from sklearn.model_selection import ShuffleSplit

execfile('python/os.py')
execfile('python/load_data_person.py')
execfile('python/clean_data_person.py')

# based on: https://github.com/eclarson/DataMiningNotebooks/blob/master/04.%20Logits%20and%20SVM.ipynb
### create a new, linear regression, dataset
print ('created new dataset for classification/logistic regression "lr"')
lr = df[important_features].copy(deep=True)

### Remove unwanted fields
del lr['POVPIP']
del lr['PUMA']

### Group "travel time"
lr.JWMNP = lr.JWMNP.fillna(-1)
lr['travel_time'] = pd.cut(lr.JWMNP, (-2, 0, 15, 40, 60, lr.JWMNP.max()), labels=['na', 'short', 'half hour', 'hour', 'long'])
del lr['JWMNP']

### Set Booleans
lr['wealthy'] = lr.affluency == 'rich'
del lr['affluency']
lr['is_male'] = lr.SEX == 'Male'
lr.is_male = lr.is_male.astype(np.int)
del lr['SEX']

### One-hot-encoding categorical - so that we have just continuous
one_hot_travel_time = pd.get_dummies(lr.travel_time, prefix='Travel_Time_')
del lr['travel_time']
one_hot_citizenship = pd.get_dummies(lr.CIT, prefix='Citizen_')
lr = pd.concat((lr, one_hot_citizenship), axis=1)
del lr['CIT']
one_hot_english = pd.get_dummies(lr.ENG, prefix='English_')
lr = pd.concat((lr, one_hot_english), axis=1)
del lr['ENG']
one_hot_worker_class = pd.get_dummies(lr.COW, prefix='Worker_Class_')
del lr['COW']

print ('After cleaning "lr" dataset:')
print (lr.info())

