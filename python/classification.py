from sklearn.model_selection import ShuffleSplit

# Create testing/training dataset - based on:
# - https://github.com/eclarson/DataMiningNotebooks/blob/master/04.%20Logits%20and%20SVM.ipynb
### create a new, linear regression, dataset
print ('created new dataset for classification/logistic regression "lr"')
lr = df.copy(deep=True)

if 'affluency' in lr:
    y = lr.affluency.values
    del lr['affluency']
    X = lr.values


### Create a testing/training set on  80% of the data, split the dataset 3 times
num_cv_iterations = 3
cv_object = ShuffleSplit(n_splits=num_cv_iterations, test_size=.2)
print ('created new dataset for testing/training classifications called "cv_object')

