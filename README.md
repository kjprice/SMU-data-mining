# SMU-data-mining

This is based on Kaggle's [2013 American Community Survey](https://www.kaggle.com/census/2013-american-community-survey) or this archived product can be [downloaded from](http://www2.census.gov/acs2013_1yr/pums/) dataset with [data dictionary](https://www2.census.gov/programs-surveys/acs/tech_docs/pums/data_dict/PUMSDataDict13.txt).

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
mkdir /data/person
mkdir /data/housing
mkdir /data/shapefiles
cd /data
wget -m https://www2.census.gov/acs2013_1yr/pums/csv_pus.zip
wget -m https://www2.census.gov/acs2013_1yr/pums/csv_hus.zip
wget -m ftp://ftp2.census.gov//geo/tiger/TIGER2013/PUMA/
cd /data/person
unzip '/data/csv_pus.zip'
cd /data/housing
unzip '/data/csv_hus.zip'
cd /data/shapefiles
unzip '/data/ftp2.census.gov/geo/tiger/TIGER2013/PUMA/*'
```

## Map:

Once you have the full list of shapes, be sure to install Basemap via `conda install basemap`. Then test out the map using `python python/map-test.py`. Output file should be found in _data/map.png_.

