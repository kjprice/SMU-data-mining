set.seed(5)

# take housing data
housing_raw_a = read.csv('../data/ss13husa.csv')
housing_raw_b = read.csv('../data/ss13husb.csv')
housing_full = rbind(housing_raw_a, housing_raw_b)

numberRowsToRetrieve = round(nrow(housing_full)*.05) # 5 percent ~73k rows
random.sample = housing_full[sample(1:nrow(housing_full), numberRowsToRetrieve, replace=FALSE),]

write.csv(random.sample, '../data/housing-subset-5percent.csv')

# take person data
person_raw_a = read.csv('../data/ss13pusa.csv')
person_raw_b = read.csv('../data/ss13pusb.csv')
person_full = rbind(person_raw_a, person_raw_b)

numberRowsToRetrieve = round(nrow(person_full)*.025) # 2.5 percent ~78k rows
random.sample = person_full[sample(1:nrow(person_full), numberRowsToRetrieve, replace=FALSE),]

write.csv(random.sample, '../data/person-subset-2.5percent.csv')
