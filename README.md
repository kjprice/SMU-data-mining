# SMU-data-mining

This is based on Kaggle's [2013 American Community Survey](https://www.kaggle.com/census/2013-american-community-survey). This archived product can be downloaded from the [census dataset](http://www2.census.gov/acs2013_1yr/pums/) with this [data dictionary](https://www2.census.gov/programs-surveys/acs/tech_docs/pums/data_dict/PUMSDataDict13.txt). With this data we hope to predict the income of various people based on several factors and to put incomes into two broad buckets: wealthy (income >= $100,00) and normal (income < $100,000).

## Predicting Personal Income

In our [final version](https://github.com/kjprice/SMU-data-mining/blob/master/python_notebooks/Project%202_Final%20Jen%20Rev.ipynb), we determined that the datasets were of unequal variance, so Logistic Regression would have skewed results. However, in the end, we determined that the most important factors, when determing someones wealth include:

 - If only speaks English `4.72`
 - If Citisen and born in the US `4.72`
 - Never served in military `4.71`
 - Married `4.63`
 - Male `4.58`

The strongest affecting wealth in a negative way:
 - If unemployed `-3.28`
 - If family receives public assistance income `-1.97`

## Setup

First download the [zipped file](https://www.kaggle.com/census/2013-american-community-survey/downloads/2013-american-community-survey.zip) for datasets. Extract files and put in [data](data) folder within this same project.

## Class Info

- Python examples from Eric Larson: https://github.com/eclarson/DataMiningNotebooks

## Map

#### Shapes:

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

Once you have the full list of shapes, be sure to install Basemap via `conda install basemap`. Then test out the map using `python python/map-test.py`. Output file should be found in _data/map.png_.

