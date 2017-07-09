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

from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn import metrics as mt
from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVC
from datetime import datetime
import matplotlib.pyplot as plt


def print_accuracy(title, results):
    accuracy = round(results.mean()*100, 2)
    std = round(results.std(), 6)
    print('%s%% accuracy (%s std) - %s' % (accuracy, std, title))

methodSpeeds = []
methodSpeedNames = []

#-------Generic function for running models---------#



def get_X_y(regression=False):
   global lr2
   ### Create reponse and explanatory variables
   lr2 = lr.copy(deep=True)
   y = list(lr2.wealthy.values)
   if regression:
       y = list(lr2.PINCP.values)
   del lr2['wealthy']
   del lr2['PINCP']
   X = lr2.values
   
   ### Standardize X values
   scl_obj = MinMaxScaler()
   scl_obj.fit(X)
   X = scl_obj.transform(X)
 
   return (X,y)


_results = []
names = []

def fit_and_test(title, model, show_individual_accuracies=False, print_confusion=False, regression=False, scoring='accuracy'):
    startTime = datetime.now()

    X, y = get_X_y(regression)
    
    cv_results = model_selection.cross_val_score(model, X, y, cv=10, scoring=scoring)
    
    _results.append(cv_results)
    names.append(title)
    
    print_accuracy(title, cv_results)

    methodSpeedNames.append(model.__class__.__name__)
    timePassed = datetime.now() - startTime
    methodSpeeds.append(timePassed.total_seconds())


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

def showSpeedPlot():
   speeds = pd.DataFrame({'method': methodSpeedNames, 'time': methodSpeeds})
   speeds.plot.bar(x='method', y='time')
showSpeedPlot()


####Visual for clustering Algorithms####
#http://hdbscan.readthedocs.io/en/latest/comparing_clustering_algorithms.html
####The use of these could be for exceptional since they are not covered in the material



####Decision Tree Regression - this is good and complete
#http://scikit-learn.org/stable/auto_examples/tree/plot_tree_regression.html

def decision_tree_regressor_example():
    dt_reg = DecisionTreeRegressor(max_depth=5)
    fit_and_test("Decision Tree Regressor", dt_reg, regression=True, scoring='r2')
    return

decision_tree_regressor_example()



####Visualization of the Decision Tree Classifier - Will this work for regression
####http://scikit-learn.org/stable/modules/tree.html

#Code that is needed for windows to find the path of the Graphviz - may not be needed by all
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin'

#Load packages for the decision tree visual
from sklearn import tree
import graphviz
import pydotplus

#Create the Tree
clf = tree.DecisionTreeClassifier()
clf = clf.fit(lr2.data, lr2.target)

with open("wealth.dot", 'w') as f:
    f = tree.export_graphviz(clf, out_file=f)
os.unlink('wealth.dot')

import pydotplus 
wealth_reg = tree.export_graphviz(clf, out_file=None) 
graph = pydotplus.graph_from_wealth_reg(wealth_reg) 
graph.write_pdf("wealth.pdf") 


#Display the decision tree in python notebook - will not display in rodeo
from IPython.display import Image  
wealth_reg = tree.export_graphviz(clf, out_file=None, 
    wealth=x,
    class_names=lr2.target_names,
    filled=True, rounded=True,  
    special_characters=True)  
graph = pydotplus.graph_from_wealth_reg(wealth_reg)  
Image(graph.create_png())



###Comparison of Algorithms
x_results = pd.Series(_results)
x_names = pd.Series(names)
def showAlgorithmMetricPlots(items_index):
    fig = plt.figure(figsize=(16,10))
    fig.suptitle('Algorithm Comparison')
    ax = fig.add_subplot(111)
    plt.boxplot(x_results[items_index])
    ax.set_xticklabels(x_names[items_index], rotation=90, fontsize=16)
    plt.show()

showAlgorithmMetricPlots(x_results.map(np.mean) > .8)



####Kernel ridge regression - - Memory Issue - - I will look at more when i return
####http://scikit-learn.org/stable/modules/generated/sklearn.kernel_ridge.KernelRidge.html#sklearn.kernel_ridge.KernelRidge
from sklearn.kernel_ridge import KernelRidge

def kernel_ridge_reg():
    kr_reg = KernelRidge(alpha=.05)
    fit_and_test("Kernel Ridge Regressor", kr_reg, regression=True, scoring='r2')
    return
   
kernel_ridge_reg()

