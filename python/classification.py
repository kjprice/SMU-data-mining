# Based on https://github.com/eclarson/DataMiningNotebooks/blob/master/04.%20Logits%20and%20SVM.ipynb

#-------Logistic Regression-------#
from sklearn.linear_model import LogisticRegression
from sklearn import metrics as mt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


### Create reponse and explanatory variables
lr2 = lr.copy(deep=True)
y = lr2.wealthy.values
del lr2['wealthy']

X = lr2.values

# y = lr.wealthy.values
# X = lr[['is_male']]
### Standardize X values
scl_obj = StandardScaler()
scl_obj.fit(X)

X = scl_obj.transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2, random_state=0)


### Create reusable logistic regression object
lr_clf = LogisticRegression(penalty='l2', C=0.05, class_weight='balanced')

### Create and test accuracy of our model
lr_clf.fit(X_train, y_train)
## TODO: use cross validation!
y_hat = lr_clf.predict(X_test)

acc = mt.accuracy_score(y_test, y_hat)
conf = mt.confusion_matrix(y_test, y_hat)

print('accuracy: %s' % acc)
print(conf)


zip_vars = zip(lr_clf.coef_.T,lr2.columns) # combine attributes
zip_vars = sorted(zip_vars)

print('\nWeights of variables')
for coef, name in zip_vars:
    print(name, 'has weight of', coef[0]) # now print them out


print('')
#----------SVM-------------#
from sklearn.model_selection import StratifiedShuffleSplit 
from sklearn.linear_model import SGDClassifier

cv = StratifiedShuffleSplit( n_splits=1,test_size=0.5)
regularize_const = 0.1
iterations = 5
svm_sgd = SGDClassifier(alpha=regularize_const, class_weight='balanced',
        fit_intercept=True, l1_ratio=0.0, learning_rate='optimal',
        loss='hinge', n_iter=iterations, n_jobs=-1, penalty='l2')

scl = StandardScaler()
for train_idx, test_idx in cv.split(X,y):
    svm_sgd.fit(scl.fit_transform(X[train_idx]),y[train_idx])
    yhat = svm_sgd.predict(scl.transform(X[test_idx]))
    
    conf = mt.confusion_matrix(y[test_idx],yhat)
    acc = mt.accuracy_score(y[test_idx],yhat)

print('SVM:', acc)

