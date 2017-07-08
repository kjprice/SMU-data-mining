## Let's see how fast bayes really is

from sklearn.naive_bayes import MultinomialNB


def create_stratified_transformed_dataset(_df):
   _df = _df.copy(deep=True)
   _df['affluency'] = pd.cut(_df.PINCP, [-1, 99999.99, 1e12], labels=('general', 'rich'))
   _df['wealthy'] = _df.affluency == 'rich'
   del _df['PINCP']
   del _df['affluency']
   
   _df = _df.fillna(-1)
   y = _df.wealthy.values
   del _df['wealthy']
   X = _df.values
   
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



df_bays = person_raw.copy(deep=True)
del df_bays['SOCP']
del df_bays['NAICSP']
del df_bays['RT']
df_bays = df_bays[df_bays.AGEP > 18]
df_bays.index = range(0, len(df))

features_for_bayes = dollar_features +\
  location_features +\
  occupation_features +\
  demographic_features +\
  personal_features +\
  relationship_features +\
  education_features +\
  military_features +\
  year_features +\
  disability_features +\
  insurance_features

bays_df = df_bays[features_for_bayes]

mb_clf = MultinomialNB(alpha=1)

test_train_data = create_stratified_transformed_dataset(bays_df)

accuracies = pd.Series()
for X_train, X_test, y_train, y_test in test_train_data:
  mb_clf.fit(X_train, y_train)
  y_hat = mb_clf.predict(X_test)

  acc = mt.accuracy_score(y_test, y_hat)
  accuracies = accuracies.append(pd.Series(acc))

print_accuracy('average accuracy for bayes', accuracies.mean(), avg=True)

