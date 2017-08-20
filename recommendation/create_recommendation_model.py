import graphlab as gl

print('try to load model')

try:
  #gl.load_model('../python_notebooks/test')
  gl.load_model('model')
  print('model available')
  quit()
except Exception:
  print('creating model')


# TODO: add song title to model
usage_data = gl.SFrame.read_csv("../data/kaggle_visible_evaluation_triplets.txt",
                                header=False,
                                delimiter='\t',
                                column_type_hints={'X3':int})


usage_data.rename({'X1':'user', 'X2': 'song_id', 'X3': 'plays'})

# TODO: Update with new params
# TODO: Display song title to user
item_item_model = gl.recommender.item_similarity_recommender.create(usage_data,
                                  user_id='user',
                                  item_id='song_id',
                                  target='plays')

item_item_model.save('model')