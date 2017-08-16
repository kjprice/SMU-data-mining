# import the library
# kernel must be [conda env:gl-env]
from matplotlib import pyplot as plt
import graphlab as gl
import graphlab.aggregate as agg
import os
import urllib

plt.style.use('ggplot')

## Download file if it does not exist
if not os.path.isfile('data/song_data.csv'):
    print('Downloading Song Data..')
    urllib.urlretrieve('https://static.turi.com/datasets/millionsong/song_data.csv', 'data/song_data.csv')
if not os.path.isfile('data/10000.txt'):
    print('Downloading 10000.txt...')
    urllib.urlretrieve('https://static.turi.com/datasets/millionsong/10000.txt', 'data/10000.txt')
##  Import data for the songs
songs = gl.SFrame.read_csv("data/song_data.csv")


# Import the data for the plays per user per song
usage_data = gl.SFrame.read_csv("data/10000.txt",
  header=False,
  delimiter='\t',
  column_type_hints={'X3':int})


# Change data labels to be human readable 
usage_data.rename({'X1':'user', 'X2': 'song', 'X3': 'plays'})


# exploratory Data Analysis


print('how many times a user might play a single song')
plays_info = usage_data['plays']
print({
    'min': plays_info.min(),
    'max': plays_info.max(),
    'mean': plays_info.mean(),
    'std': plays_info.std()
})

## TODO: Perhaps use a violin plot / or apply log scale to "Count" attribute
number_plays = usage_data.groupby('plays', [ag.COUNT()]).to_dataframe()
number_plays.sort('plays').plot.bar()



# Make the first recommendation 
# because the parameter "target" exists, we know that this is a user-item recommendation
# https://turi.com/products/create/docs/generated/graphlab.recommender.create.html#graphlab.recommender.create
model = gl.recommender.create(usage_data, user_id = "user", item_id="song", target = "plays")
results = model.recommend(users=None, k=5)
model.save("my_model")


## Split data (cross validation)
train, test = gl.recommender.util.random_split_by_user(usage_data, 'user', 'song')



# Make another recommendation, this time item-item
item_item = gl.recommender.item_similarity_recommender.create(train,
                                                             user_id="user",
                                                             item_id="song",
                                                             target="plays",
                                                             only_top_k=3,
                                                             similarity_type="cosine")

results = item_item.get_similar_items(k=3)
results.head



## TODO: compare RMSE, precision and recall
## TODO: compare item-item and user-item models
## TODO: Use automated parameter-picking techniques

## cross validation
rec_cv = gl.recommender.ranking_factorization_recommender.create(train,
                                                        user_id='user',
                                                        item_id='song',
                                                        target='plays'
                                                        )


results_from_rmse = rec_cv.evaluate(test)

results_from_rmse['precision_recall_by_user'].groupby('cutoff',[agg.AVG('precision'),agg.STD('precision'),agg.AVG('recall'),agg.STD('recall')])



## Let's find the best params
params = {
    'user_id': 'user',
    'item_id': 'song',
    'target': 'plays',
    'num_factors': [8, 12, 16, 24, 32], 
    'regularization':[0.001, .01],
    'linear_regularization': [0.001, .01]
}

job = gl.model_parameter_search.create( (train,test),
    gl.recommender.ranking_factorization_recommender.create,
    params,
    max_models=5,
    environment=None
)


job.get_status()

job_results = job.get_results()

job_results.head()


best_prms = job.get_best_params()
best_prms

models = job.get_models()
models

comparisonstruct = gl.compare(test,models)
gl.show_comparison(comparisonstruct,models)







