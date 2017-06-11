# Based on https://github.com/eclarson/DataMiningNotebooks/blob/master/04.%20Logits%20and%20SVM.ipynb
# Logistic Regression
from sklearn.linear_model import LogisticRegression
from sklearn import metrics as mt

### Create reponse and explanatory variables
y = lr.wealthy.values
X = lr.values


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
    
    