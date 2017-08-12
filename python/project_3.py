# import the library
# kernel must be [conda env:gl-env]
import graphlab as gl
import os
import urllib

## Download file if it does not exist
if not os.path.isfile('data/song_data.csv'):
    print('Downloading Song Data..')
    %time urllib.urlretrieve('https://static.turi.com/datasets/millionsong/song_data.csv', 'data/song_data.csv')
if not os.path.isfile('../data/10000.txt'):
    print('Downloading 10000.txt...')
    %time urllib.urlretrieve('https://static.turi.com/datasets/millionsong/10000.txt', 'data/10000.txt')
##  Import data for the songs
songs = gl.SFrame.read_csv("data/song_data.csv")


# Import the data for the plays per user per song
usage_data = gl.SFrame.read_csv("data/10000.txt",
  header=False,
  delimiter='\t',
  column_type_hints={'X3':int})


# Change data labels to be human readable 
usage_data.rename({'X1':'user', 'X2': 'song', 'X3': 'plays'})




# Make the first recommendation 
# because the parameter "target" exists, we know that this is a user-item recommendation
# https://turi.com/products/create/docs/generated/graphlab.recommender.create.html#graphlab.recommender.create
model = gl.recommender.create(usage_data, user_id = "user", item_id="song", target = "plays")
results = model.recommend(users=None, k=5)
model.save("my_model")

print(results.head())




# Make another recommendation, this time item-item
item_item = gl.recommender.item_similarity_recommender.create(usage_data,
                                                             user_id="user",
                                                             item_id="song",
                                                             target="plays",
                                                             only_top_k=3,
                                                             similarity_type="cosine")

results = item_item.get_similar_items(k=3)
results.head

