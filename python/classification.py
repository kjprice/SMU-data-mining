# Based on https://github.com/eclarson/DataMiningNotebooks/blob/master/04.%20Logits%20and%20SVM.ipynb

#-------Logistic Regression-------#
from sklearn.linear_model import LogisticRegression
from sklearn import metrics as mt
from sklearn.model_selection import cross_val_score


### Create reponse and explanatory variables
lr2 = lr.copy(deep=True)
y = lr2.wealthy.values
del lr2['wealthy']

X = lr2.values

### Create a testing/training set on  80% of the data, split the dataset 3 times
num_cv_iterations = 3
cv_object = ShuffleSplit(n_splits=num_cv_iterations, test_size=.2)
print ('created new dataset for testing/training classifications called "cv_object')


### Create reusable logistic regression object
lr_clf = LogisticRegression(penalty='l2', C=1.0, class_weight=None)

### Create and test accuracy of our model
accuracies = cross_val_score(lr_clf, X, y=y, cv=cv_object) # this also can help with parallelism
print(accuracies)


print('')
#----------SVM-------------#
from sklearn.model_selection import StratifiedShuffleSplit 
from sklearn.linear_model import SGDClassifier
from sklearn.preprocessing import StandardScaler

cv = StratifiedShuffleSplit( n_splits=1,test_size=0.5)
regularize_const = 0.1
iterations = 5
svm_sgd = SGDClassifier(alpha=regularize_const,
        fit_intercept=True, l1_ratio=0.0, learning_rate='optimal',
        loss='hinge', n_iter=iterations, n_jobs=-1, penalty='l2')

scl = StandardScaler()
for train_idx, test_idx in cv.split(X,y):
    svm_sgd.fit(scl.fit_transform(X[train_idx]),y[train_idx])
    yhat = svm_sgd.predict(scl.transform(X[test_idx]))
    
    conf = mt.confusion_matrix(y[test_idx],yhat)
    acc = mt.accuracy_score(y[test_idx],yhat)

print('SVM:', acc)

