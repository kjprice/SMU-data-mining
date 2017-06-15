# Based on https://github.com/eclarson/DataMiningNotebooks/blob/master/04.%20Logits%20and%20SVM.ipynb

#-------Logistic Regression-------#
from sklearn.linear_model import LogisticRegression
from sklearn import metrics as mt

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

iter_num = 0

### Create and test accuracy of our model
for train_indices, test_indices in cv_object.split(X,y):
    X_train = X[train_indices]
    y_train = y[train_indices]
    
    X_test = X[test_indices]
    y_test = y[test_indices]
    
    lr_clf.fit(X_train, y_train)
    y_hat = lr_clf.predict(X_test)
    
    acc = mt.accuracy_score(y_test, y_hat)

    print("====Iteration",iter_num," ====")
    print('accuracy', acc)
    iter_num += 1

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

