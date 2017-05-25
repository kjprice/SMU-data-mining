set.seed(5)

# take housing data
housing_raw_a = read.csv('../data/ss13husa.csv')
housing_raw_b = read.csv('../data/ss13husb.csv')
housing_full = rbind(housing_raw_a, housing_raw_b)

numberRowsToRetrieve = round(nrow(housing_full)*.05) # 5 percent
random.sample = housing_full[sample(1:nrow(housing_full), numberRowsToRetrieve, replace=FALSE),]

write.csv(random.sample, '../data/housing-subset-5percent.csv')
