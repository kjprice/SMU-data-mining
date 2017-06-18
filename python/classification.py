# Based on https://github.com/eclarson/DataMiningNotebooks/blob/master/04.%20Logits%20and%20SVM.ipynb

#-------Logistic Regression-------#
from sklearn.linear_model import LogisticRegression
from sklearn import metrics as mt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def clean_data_for_analysis():
   global lr2
   ### Create reponse and explanatory variables
   lr2 = lr.copy(deep=True)
   y = lr2.wealthy.values
   del lr2['wealthy']
   X = lr2.values

   ### Standardize X values
   scl_obj = StandardScaler()
   scl_obj.fit(X)
   X = scl_obj.transform(X)
   
   ### Get training/test data
   return train_test_split(X, y, test_size=.2, random_state=0)

X_train, X_test, y_train, y_test = clean_data_for_analysis()

def run_logistic_regression():
   ### Create reusable logistic regression object
   global lr_clf
   lr_clf = LogisticRegression(penalty='l2', C=0.05, class_weight='balanced')
   
   ### Create and test accuracy of our model
   lr_clf.fit(X_train, y_train)
   ## TODO: use cross validation!
   y_hat = lr_clf.predict(X_test)
   
   acc = mt.accuracy_score(y_test, y_hat)
   conf = mt.confusion_matrix(y_test, y_hat)
   
   print('accuracy: %s' % acc)
   print(conf)

run_logistic_regression()


### Get weights
def get_weights():
   zip_vars = zip(lr_clf.coef_.T, lr2.columns) # combine attributes
   zip_vars = sorted(zip_vars)
   
   print('\nWeights of variables')
   for coef, name in zip_vars:
       print(name, 'has weight of', coef[0]) # now print them out

get_weights()

print('')
#----------SVM-------------#

### Using Batch Gradient Descent, we get accuracy of 78.2% (compared to 77.2% using SGD), but it takes 3 minutes to calculate
from sklearn.svm import SVC

def bgd():
   from datetime import datetime
   startTime = datetime.now()
   
   svm_clf = SVC(C=0.5, class_weight='balanced')
   svm_clf.fit(X_train, y_train)
   
   y_hat = svm_clf.predict(X_test)
   
   conf = mt.confusion_matrix(y_test, y_hat)
   acc = mt.accuracy_score(y_test,y_hat)
   
   print('SVM:', acc)
   print (datetime.now() - startTime)

#bgd()

### Using SGD
from sklearn.model_selection import StratifiedShuffleSplit 
from sklearn.linear_model import SGDClassifier

def run_sgd():
   regularize_const = 0.1
   iterations = 5
   svm_sgd = SGDClassifier(alpha=regularize_const, class_weight='balanced',
           fit_intercept=True, l1_ratio=0.0, learning_rate='optimal',
           loss='hinge', n_iter=iterations, n_jobs=-1, penalty='l2')
   
   svm_sgd.fit(X_train, y_train)
   y_hat = svm_sgd.predict(X_test)
   
   acc = mt.accuracy_score(y_test, y_hat)
   conf = mt.confusion_matrix(y_test, y_hat)
   
   print('accuracy: %s \n' % acc)

run_sgd()




####Create series of the weights and map
from matplotlib import pyplot as plt
%matplotlib inline
plt.style.use('ggplot')

weights = pd.Series(lr_clf.coef_[0],index=lr2.columns)
print weights
weights.plot(kind='bar')
plt.show()







