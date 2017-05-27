df = person_raw.copy(deep=True)

dollarFeatures = [
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

locationFeatures = [
    'PUMA', # Public use microdata area code (PUMA) based on 2010 Census definition
    'MIGPUMA', # Migration PUMA based on 2010 Census definition
    'POWPUMA', # Place of work PUMA based on 2010 Census definition
    'ST', # State Code
]
occupationFeatures = [
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
    'SCIENGP', # Field of Degree Science and Engineering Flag – NSF Definition
    'WRK', # Worked last week
    'COW', # Class of worker
    'NWLA', # On layoff from work
    'NWLK', # Looking for work

]

demographicFeatures = [
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

personalFeatures = [
    'PWGTP', # Person's weight
    'POVPIP', # Income-to-poverty ratio recode
    'SPORDER', # Person number
    'QTRBIR', # Quarter of birth
    'SEX', # Sex
]

relationshipFeatures = [
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

educationFeatures = [
    'SCHL', # Educational attainment
    'SCHG', # Grade level attending
    'SCIENGRLP', # Field of Degree Science and Engineering Related Flag – NSF Definition
]

militaryFeatures = [
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

yearFeatures = [
    'CITWP', # Year of naturalization write-in
    'MARHYP', # Year last married
    'YOEP', # Year of entry
]

disabilityFeatures = [
    'DDRS', # Self-care difficulty
    'DEAR', # Hearing difficulty
    'DEYE', # Vision difficulty
    'DIS', # Disability recode
    'DOUT', # Independent living difficulty
    'DPHY', # Ambulatory difficulty
    'DRATX', # Veteran service connected disability rating (checkbox)
    'DREM', # Cognitive difficulty
]

insuranceFeatures = [
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

