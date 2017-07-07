df = person_raw.copy(deep=True)

df = df[df.AGEP > 18]

### This seems to be necessary to make stacked barplots on one feature
df.dummy = True

### Define important features
important_continuous_features = [
    'PINCP',    # Total person's income (signed)
    'POVPIP',   # Income-to-poverty ratio recode (continuous)
    'JWMNP',    # Travel time to work (continuous)
    'AGEP',     # Age of person (continuous 0-95)
    'PWGTP',    # Person's weight (continuous)
    'PAP',      # Public assistance income in past 12 months
]
importegorical_features = [
    'CIT',  # Citizenship status (categorical - string)
    'ENG',  # Ability to speak English (ordinal 1-4)
    'COW',      # Class of worker (categorical - string)
    'PUMA',     # Public use microdata area code (PUMA) based on 2010 Census definition
    'SEX',      # Gender
    'MIL',      # Military Service
    'SCHL',     # Level of Education Attained
    'MAR'       # Marital Status
]
important_features = important_continuous_features + importegorical_features;

dollar_features = [
    'PINCP', # Total person's income (signed)
    'PERNP', # Total person's earnings
    'ADJINC', # Adjustment factor for income and earnings dollar amounts (6 implied decimal places)
    'WAGP', # Wages or salary income past 12 months
    'SEMP', # Self-employment income past 12 months (signed)
    'INTP', # Interest, dividends, and net rental income past 12 months (signed)
    'RETP', # Retirement income past 12 months
    'OIP', # All other income past 12 months
    'SSP', # Social Security income past 12 months
    'PAP', # Public assistance income past 12 months
    'SSIP', # Supplementary Security Income past 12 months
]

location_features = [
    'PUMA', # Public use microdata area code (PUMA) based on 2010 Census definition
    'MIGPUMA', # Migration PUMA based on 2010 Census definition
    'POWPUMA', # Place of work PUMA based on 2010 Census definition
    'ST', # State Code
]

occupation_features = [
    'INDP', # Industry recode for 2013 and later based on 2012 IND codes
    'OCCP', # Occupation recode for 2012 and later based on 2010 OCC codes
    'POWSP', # Place of work - State or foreign country recode
    'JWAP', # Time of arrival at work - hour and minute
    'JWMNP', # Travel time to work
    'JWDP', # Time of departure for work - hour and minute
    'WKHP', # Usual hours worked per week past 12 months
    'RAC2P', # Recoded detailed race code
    'JWTR', # Means of transportation to work
    'JWRIP', # Vehicle occupancy
    'ESP', # Employment status of parents
    'DRIVESP', # Number of vehicles calculated from JWRI
    'ESR', # Employment status recode
    'WKW', # Weeks worked during past 12 months
    'NWAV', # Available for work
    'NWAB', # Temporary absence from work
    'NWRE', # Informed of recall
    'SCH', # School enrollment
    'SFN', # Subfamily number
    'WKL', # When last worked
    'SCIENGP', # Field of Degree Science and Engineering Flag - NSF Definition
    'WRK', # Worked last week
    'COW', # Class of worker
    'NWLA', # On layoff from work
    'NWLK', # Looking for work

]

demographic_features = [
    'ANC1P', # Recoded Detailed Ancestry - first entry
    'ANC2P', # Recoded Detailed Ancestry - second entry
    'LANP', # Language spoken at home
    'MIGSP', # Migration recode - State or foreign country code
    'POBP', # Place of birth (Recode)
    'RAC3P', # Recoded detailed race code
    'AGEP', # Age
    'HISP', # Recoded detailed Hispanic origin
    'RAC1P', # Recoded detailed race code
    'NOP', # Nativity of parent
    'DECADE', # Decade of entry
    'CIT', # Citizenship status
    'RACNUM', # Number of major race groups represented
    'ENG', # Ability to speak English
    'LANX', # Language other than English spoken at home
    'NATIVITY', # Nativity
    'RACAIAN', # American Indian and Alaska Native recode (American Indian and
    'RACASN', # Asian recode (Asian alone or in combination with one or more
    'RACBLK', # Black or African American recode (Black alone or in
    'RACNH', # Native Hawaiian recode (Native Hawaiian alone or in combination with
    'RACPI', # Other Pacific Islander recode (Other Pacific Islander alone or in
    'RACSOR', # Some other race recode (Some other race alone or in
    'RACWHT', # White recode (White alone or in combination with one or more
    'WAOB', # World area of birth

]

personal_features = [
    'PWGTP', # Person's weight
    'POVPIP', # Income-to-poverty ratio recode
    'SPORDER', # Person number
    'QTRBIR', # Quarter of birth
    'SEX', # Sex
]

relationship_features = [
    'RELP', # Relationship
    'MSP', # Married, spouse present/spouse absent
    'GCM', # Length of time responsible for grandchildren
    'MAR', # Marital status
    'PAOC', # Presence and age of own children
    'MARHT', # Number of times married
    'FER', # Gave birth to child within the past 12 months
    'GCL', # Grandparents living with grandchildren
    'GCR', # Grandparents responsible for grandchildren
    'MARHD', # Divorced in the past 12 months
    'MARHM', # Married in the past 12 months
    'MARHW', # Widowed in the past 12 months
    'OC', # Own child
    'RC', # Related child
]

education_features = [
    'SCHL', # Educational attainment
    'SCHG', # Grade level attending
    'SCIENGRLP', # Field of Degree Science and Engineering Related Flag - NSF Definition
]

military_features = [
    'VPS', # Veteran period of service
    'DRAT', # Veteran service connected disability rating (percentage)
    'MIL', # Military service
    'MLPA', # Served September 2001 or later
    'MLPB', # Served August 1990 - August 2001 (including Persian Gulf War)
    'MLPCD', # Served May 1975 - July 1990
    'MLPE', # Served Vietnam era (August 1964 - April 1975)
    'MLPFG', # Served February 1955 - July 1964
    'MLPI', # Served January 1947 - June 1950
    'MLPH', # Served Korean War (July 1950 - January 1955)
    'MLPK', # Served November 1941 or earlier
    'MLPJ', # Served World War II (December 1941 - December 1946)
]

year_features = [
    'CITWP', # Year of naturalization write-in
    'MARHYP', # Year last married
    'YOEP', # Year of entry
]

disability_features = [
    'DDRS', # Self-care difficulty
    'DEAR', # Hearing difficulty
    'DEYE', # Vision difficulty
    'DIS', # Disability recode
    'DOUT', # Independent living difficulty
    'DPHY', # Ambulatory difficulty
    'DRATX', # Veteran service connected disability rating (checkbox)
    'DREM', # Cognitive difficulty
]

insurance_features = [
    'HICOV', # Health insurance coverage recode
    'HINS1', # Insurance through a current or former employer or union
    'HINS2', # Insurance purchased directly from an insurance company
    'HINS3', # Medicare, for people 65 and older, or people with certain disabilities
    'HINS4', # Medicaid, Medical Assistance, or any kind of government-assistance plan
    'HINS5', # TRICARE or other military health care
    'HINS6', # VA (including those who have ever used or enrolled for VA health care)
    'HINS7', # Indian Health Service
    'PRIVCOV', # Private health insurance coverage recode
    'PUBCOV', # Public health coverage recode
]








# Clean important features
### Change from numeric to categorical (ordinal)
df['CIT'] = df.CIT.astype('category').astype('str')
df.CIT = df.CIT \
    .replace('1', 'US Born') \
    .replace('2', 'US Territory Born') \
    .replace('3', 'Born Abroad)') \
    .replace('4', 'Naturalized') \
    .replace('5', 'Non-Citizen')

df['OC'] = df.OC.astype('category').astype(bool)

df['ENG'] = df.ENG.astype('category').astype('str')
df.ENG = df.ENG \
    .replace('nan', 'Speaks only English') \
    .replace('1.0', 'Very well') \
    .replace('2.0', 'Well') \
    .replace('3.0', 'Not well') \
    .replace('4.0', 'Not at all')

df['COW'] = df.COW.astype('category').astype('str')
df.COW = df.COW \
    .replace('b', 'child') \
    .replace('1.0', 'Private for Profit') \
    .replace('2.0', 'Private Non-Profit') \
    .replace('3.0', 'Local Government') \
    .replace('4.0', 'State Government') \
    .replace('5.0', 'Federal Government') \
    .replace('6.0', 'Self Employed (not incorportated)') \
    .replace('7.0', 'Self Employed (incorporated)') \
    .replace('8.0', 'Family Business - no pay') \
    .replace('9.0', 'Unemployeed')

df['JWTR'] = df.JWTR.astype('category').astype('str')
df.JWTR = df.JWTR \
    .replace('1.0', 'Car, truck, or van') \
    .replace('2.0', 'Bus or trolley bus') \
    .replace('3.0', 'Streetcar or trolley car') \
    .replace('4.0', 'Subway or elevated') \
    .replace('5.0', 'Railroad') \
    .replace('6.0', 'Ferryboat') \
    .replace('7.0', 'Taxicab') \
    .replace('8.0', 'Motorcycle') \
    .replace('9.0', 'Bicycle') \
    .replace('10.0', 'Walked') \
    .replace('11.0', 'Worked at home') \
    .replace('12.0', 'Other method') \
    .replace('nan', 'Non-Commuter (unemployed, child, military)')

df['PUMA'] = df.PUMA.astype('category')
df['ST'] = df.ST.astype('category').astype('str')
df.ST = df.ST \
    .replace('1', 'AL') \
    .replace('2', 'AK') \
    .replace('4', 'AZ') \
    .replace('5', 'AR') \
    .replace('6', 'CA') \
    .replace('8', 'CO') \
    .replace('9', 'CT') \
    .replace('10', 'DE') \
    .replace('11', 'DC') \
    .replace('12', 'FL') \
    .replace('13', 'GA') \
    .replace('15', 'HI') \
    .replace('16', 'ID') \
    .replace('17', 'IL') \
    .replace('18', 'IN') \
    .replace('19', 'IA') \
    .replace('20', 'KS') \
    .replace('21', 'KY') \
    .replace('22', 'LA') \
    .replace('23', 'ME') \
    .replace('24', 'MD') \
    .replace('25', 'MA') \
    .replace('26', 'MI') \
    .replace('27', 'MN') \
    .replace('28', 'MS') \
    .replace('29', 'MO') \
    .replace('30', 'MT') \
    .replace('31', 'NE') \
    .replace('32', 'NV') \
    .replace('33', 'NH') \
    .replace('34', 'NJ') \
    .replace('35', 'NM') \
    .replace('36', 'NY') \
    .replace('37', 'NC') \
    .replace('38', 'ND') \
    .replace('39', 'OH') \
    .replace('40', 'OK') \
    .replace('41', 'OR') \
    .replace('42', 'PA') \
    .replace('44', 'RI') \
    .replace('45', 'SC') \
    .replace('46', 'SD') \
    .replace('47', 'TN') \
    .replace('48', 'TX') \
    .replace('49', 'UT') \
    .replace('50', 'VT') \
    .replace('51', 'VA') \
    .replace('53', 'WA') \
    .replace('54', 'WV') \
    .replace('55', 'WI') \
    .replace('56', 'WY') \
    .replace('72', 'PR')

df['GCL'] = df.GCL.astype('category').astype('str')
df.GCL = df.GCL \
    .replace('1.0', 'Grandparents living with Grandchildren') \
    .replace('2.0', 'Grandparents do not live with grandchildren') \
    .replace('nan', 'less than 30 years old')

df['MAR'] = df.MAR.astype('category').astype('str')
df.MAR = df.MAR \
    .replace('1', 'Married') \
    .replace('2', 'Widowed') \
    .replace('3', 'Divorced') \
    .replace('4', 'Separated') \
    .replace('5', 'Never Married') 

df['SEX'] = df.SEX.astype('category').astype('str')
df.SEX = df.SEX \
    .replace('1', 'Male') \
    .replace('2', 'Female') 

df['MIL'] = df.MIL.astype('category').astype('str')
df.MIL = df.MIL \
    .replace('1.0', 'Serving Active Duty') \
    .replace('2.0', 'Served Not Active') \
    .replace('3.0', 'Reserves') \
    .replace('4.0', 'Never Served')

# Take rows where income is less than $150,000
df_small_income = df[df.PINCP < 150000]













