# Based on https://github.com/eclarson/DataMiningNotebooks/blob/master/04.%20Logits%20and%20SVM.ipynb

### Possible classification techniques:
# Naive Bayes
# KNN
# Decision Trees
# Logistic Regression
# SVM
# GD

import numpy as np 
import pandas as pd
import seaborn as sns

from sklearn.linear_model import LogisticRegression
from sklearn import metrics as mt
from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.ensemble import RandomForestClassifier

def print_accuracy(title, accuracy, avg=False):
    accuracy = round(accuracy*100, 2)
    avg_text = 'avg' if avg else ''
    bullet = ''
    if not avg:
       bullet = '**'
    print('%s%s%% %s accuracy - %s' % (bullet, accuracy, avg_text, title))



#-------Generic function for running models---------#

def fit_and_test(title, test_train, show_individual_accuracies=False, print_confusion=False):
   accuracies = pd.Series()
   for X_train, X_test, y_train, y_test in test_train_data:
      test_train.fit(X_train, y_train)
      y_hat = test_train.predict(X_test)
      
      acc = mt.accuracy_score(y_test, y_hat)
      accuracies = accuracies.append(pd.Series(acc))
      
      if print_confusion:
         print(mt.confusion_matrix(y_test, y_hat))
      
      if show_individual_accuracies:
         print_accuracy(title, acc)
   print_accuracy(title, accuracies.mean(), avg=True)



#-------Decision Tree-------#
def run_decision_tree(max_features):
   dt_clf = DecisionTreeClassifier(max_features=max_features, class_weight='balanced')
   fit_and_test('decision tree', dt_clf)


run_decision_tree(max_features=None)
run_decision_tree(max_features=4)

dt_clf = RandomForestClassifier(class_weight='balanced')
fit_and_test('Random Forest', dt_clf)


print('')

#-------Bayes-------#
def run_multinomial_bayes(alpha):
    mb_clf = MultinomialNB(alpha=alpha)
    fit_and_test('bayes multinomial %s'%(alpha), mb_clf, show_individual_accuracies=False)

run_multinomial_bayes(100)
run_multinomial_bayes(1)
run_multinomial_bayes(.01)

print('')


def run_bernoulli_bayes(alpha, binarize=.0):
    # TODO: tweak alpha
    mb_clf = BernoulliNB(alpha=alpha, binarize = binarize)
    title_with_params = 'bayes bernoulli %s, %s' % (alpha, binarize)
    
    fit_and_test(title_with_params, mb_clf, show_individual_accuracies=False)

run_bernoulli_bayes(10000)
run_bernoulli_bayes(.1)
run_bernoulli_bayes(10000, 1)
run_bernoulli_bayes(.1, 1)

print('')


def run_gaussian_bayes():
    # TODO: tweak alpha
    mb_clf = GaussianNB()
    fit_and_test('bayes gaussian', mb_clf, show_individual_accuracies=False)

run_gaussian_bayes()

print('')


#-------Logistic Regression-------#
def run_logistic_regression():
   ### Create reusable logistic regression object
   global lr_clf
   lr_clf = LogisticRegression(penalty='l2', C=0.05, class_weight='balanced')
   fit_and_test('logistic regression', lr_clf, show_individual_accuracies=False)
   # print(conf)

run_logistic_regression()


### Get weights
def get_weights():
   zip_vars = zip(lr_clf.coef_.T, lr2.columns) # combine attributes
   zip_vars = sorted(zip_vars)
   
   print('\nWeights of variables')
   for coef, name in zip_vars:
       print(name, 'has weight of', coef[0]) # now print them out

   print('')

# get_weights()
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
   
   explain_SV(svm_clf)

#bgd()

### Using SGD

def run_sgd():
   regularize_const = 0.1
   iterations = 5
   svm_sgd = SGDClassifier(alpha=regularize_const, class_weight='balanced',
           fit_intercept=True, l1_ratio=0.0, learning_rate='optimal',
           loss='hinge', n_iter=iterations, n_jobs=-1, penalty='l2')
   
   fit_and_test('gradient descent', svm_sgd, show_individual_accuracies=False)

run_sgd()

#----------KNN-------------#
def run_knn():
    ## seems to default to kd_tree
    ## TODO: see if parameters can be used to tweak
    knn_clf = KNeighborsClassifier()
    fit_and_test('knn', knn_clf, show_individual_accuracies=False)

# run_knn()


####Create series of the weights and map
def plot_series_of_weights():
   from matplotlib import pyplot as plt
   %matplotlib inline
   plt.style.use('ggplot')
   
   weights = pd.Series(lr_clf.coef_[0],index=lr2.columns)
   # print weights
   weights.plot(kind='bar')
   plt.show()
#plot_series_of_weights()
   
##Re-creating the training set with Wealthy
lr2 = lr.copy(deep=True)
y = lr2.wealthy.values
X = lr2.values

# Analysis of Support Vectors

def explain_SV(svm_clf):
   # make a dataframe of the training data
   # df_tested_on = pd.DataFrame(X_train) # saved from above, the indices chosen for training
   df_tested_on = lr2
   # now get the support vectors from the trained model
   df_support = df_tested_on.iloc[svm_clf.support_,:]
   
   df_support.loc[:,'wealthy'] = y[svm_clf.support_] # add back in the 'Survived' Column to the pandas dataframe
   lr2.loc[:,'wealthy'] = y # also add it back in for the original data
   df_support.info()
   
   
   # now lets see the statistics of these attributes
   from pandas.tools.plotting import boxplot
   
   # group the original data and the support vectors
   df_grouped_support = df_support.groupby(['wealthy'])
   df_grouped = lr2.groupby(['wealthy'])
   
   # plot KDE of Different variables
   vars_to_plot = ['AGEP']
   
   for v in vars_to_plot:
       plt.figure(figsize=(10,4))
       # plot support vector stats
       plt.subplot(1,2,1)
       ax = df_grouped_support[v].plot.kde() 
       plt.legend(['not_wealthy','wealthy'])
       plt.title(v+' (Instances chosen as Support Vectors)')
       
       # plot original distributions
       plt.subplot(1,2,2)
       ax = df_grouped[v].plot.kde() 
       plt.legend(['not_wealthy','wealthy'])
       plt.title(v+' (Original)')
   
   # create_join_plot(svm_clf)

def create_join_plot(svm_clf):
   #### Create jointplot
   
   #array of the support vectors from the SVM
   SVM_support_vectors = svm_clf.support_vectors_
   #print(SVM_support_vectors)
   
   ####NEEDS WORK.   NEED 2 CONTINUOUS VARIABLES.  ABLE TO GET THE SUPPORT VECTORS, BUT THE AGE IS NOT IN SAME DATASET
   np.random.seed(0)
   sns.set(style="white", color_codes=True)
   tips = sns.load_dataset("tips")
   g = sns.jointplot(x="AGEP", y="SVM_support_vectors", data=svm_clf)


