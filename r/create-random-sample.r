set.seed(5)

numberRowsToRetrieve = round(nrow(housing_raw)*.10) # 10 percent
random.sample = housing_raw[sample(1:nrow(housing_raw), numberRowsToRetrieve, replace=FALSE),]

write.csv(random.sample, '../data/housing-subset-10percent.csv')
