# SMU-data-mining

This is based on Kaggle's [2013 American Community Survey](https://www.kaggle.com/census/2013-american-community-survey) dataset.

## Setup

Download [zipped file](https://www.kaggle.com/census/2013-american-community-survey/downloads/2013-american-community-survey.zip) for datasets. Extract files and put in [data](data) folder.

## Class Info

- Python examples from Eric Larson: https://github.com/eclarson/DataMiningNotebooks
- Information from Yuhang Wang: https://drive.google.com/drive/folders/0ByOvNZ5dj09yM0gzaTBVZHNIV28?usp=sharing  

## TODOs:

If we are going to use PCA - be sure to scale the data. Use `from sklearn.preprocessing import StandardScalar`

## Shapes:

The shape files from the zipped data appear to be limited. It is missing data from the first 31 states. To get the real shape files, you can get them from source via ftp. I built a little script that should pull it all for you recursively:

```sh
wget -m ftp://ftp2.census.gov//geo/tiger/TIGER2013/PUMA/
mkdir output
cd output
unzip '../ftp2.census.gov/geo/tiger/TIGER2013/PUMA/*'
```

## Map:

Once you have the full list of shapes, be sure to install Basemap via `conda install basemap`. Then test out the map using `python python/map-test.py`. Output file should be found in _data/map.png_.

