from sklearn.model_selection import StratifiedKFold

# based on: https://github.com/eclarson/DataMiningNotebooks/blob/master/04.%20Logits%20and%20SVM.ipynb
### create a new, linear regression, dataset
lr = df[important_features].copy(deep=True)

### Remove unwanted fields
del lr['POVPIP']
del lr['PUMA']
del lr['PINCP']

### Group "travel time"
lr.JWMNP = lr.JWMNP.fillna(-1)
lr['travel_time'] = pd.cut(lr.JWMNP, (-2, 0, 15, 40, 60, lr.JWMNP.max()), labels=['na', 'short', 'half hour', 'hour', 'long'])
del lr['JWMNP']

### Group "education attained"
lr.SCHL = lr.SCHL.fillna(-1)
lr['education_attained'] = pd.cut(lr.SCHL, (-2, 1, 11, 15, 17, 20, 21, 22, 23, 24), labels=['na', 'no_high_school', 'some_high_school', 'HS_diploma', 'some_college', 'bacholors_degree', 'masters_degree', 'professional_degree', 'doctorate_degree'])
del lr['SCHL']


### Set Booleans
lr['wealthy'] = lr.affluency == 'rich'
del lr['affluency']
lr['is_male'] = lr.SEX == 'Male'
lr.is_male = lr.is_male.astype(np.int)
del lr['SEX']

### One-hot-encoding categorical - so that we have just continuous
one_hot_travel_time = pd.get_dummies(lr.travel_time, prefix='Travel_Time_')
lr = pd.concat((lr, one_hot_travel_time), axis=1)
del lr['travel_time']

one_hot_citizenship = pd.get_dummies(lr.CIT, prefix='Citizen_')
lr = pd.concat((lr, one_hot_citizenship), axis=1)
del lr['CIT']

one_hot_english = pd.get_dummies(lr.ENG, prefix='English_')
lr = pd.concat((lr, one_hot_english), axis=1)
del lr['ENG']

one_hot_worker_class = pd.get_dummies(lr.COW, prefix='Worker_Class_')
lr = pd.concat((lr, one_hot_worker_class), axis=1)
del lr['COW']

one_hot_military = pd.get_dummies(lr.MIL, prefix='Miliary_Service_')
lr = pd.concat((lr, one_hot_military), axis=1)
del lr['MIL']

one_hot_education_attained = pd.get_dummies(lr.education_attained, prefix='Education_Attained_')
lr = pd.concat((lr, one_hot_education_attained), axis=1)
del lr['education_attained']

one_hot_marital_status = pd.get_dummies(lr.MAR, prefix="Marital_status_")
lr = pd.concat((lr, one_hot_marital_status), axis=1)
del lr['MAR']





#-------Stratified K Fold---------#
def create_stratified_transformed_dataset():
   global lr2
   ### Create reponse and explanatory variables
   lr2 = lr.copy(deep=True)
   y = lr2.wealthy.values
   del lr2['wealthy']
   X = lr2.values
   
   ### Standardize X values
   scl_obj = MinMaxScaler()
   scl_obj.fit(X)
   X = scl_obj.transform(X)
   
   skf = StratifiedKFold(n_splits=10)

   skf.get_n_splits(X, y)
   
   _data = []
   for train_index, test_index in skf.split(X, y):
      X_train, X_test = X[train_index], X[test_index]
      y_train, y_test = y[train_index], y[test_index]
      _data.append([X_train, X_test, y_train, y_test])
      
   return _data


test_train_data = create_stratified_transformed_dataset()








