### Create main working data frame
df = housing_raw.copy(deep=True)


#### Group features together - sorted by max-value desc

dollarFeatures = [
   'ADJINC',
   'ADJHSG',
   'SMOCP',
   'MHP',
   'INSP',
   'MRGP',
   'FULP',
   'GRNTP',
   'WATP',
   'RNTP',
   'SMP', # Total payment on all second and junior mortgages and home equity loans
   'WGTP', 
   'CONP', # Condo fee
   'ELEP',
   'GASP',
   'GRPIP',
   'OCPIP',
   'TAXP'
]

incomeDollarFeatures = [
   'ADJINC',
   'ADJHSG',
]

costDollarFeatures = [
   'SMOCP',
   'MHP',
   'INSP',
   'MRGP',
   'FULP',
   'GRNTP',
   'WATP',
   'RNTP',
   'SMP', # Total payment on all second and junior mortgages and home equity loans
   'WGTP', 
   'CONP', # Condo fee
   'ELEP',
   'GASP',
   'GRPIP',
   'OCPIP',
   'TAXP'
]

locationFeatures = [
   'PUMA',
   'ST', # State
   'DIVISION', # Specific region in country (0-9)
   
]

houseFeatures = [
   'RMSP', # Number of Rooms
   'BDSP', # Number of bedrooms
   'YBL', # Year home was built
   'HFL', # Type of heat
   'BLD', # Units in structure
   'RWATPR', # Running Water Exists
   'VACS', # Vacancy status (b, 1-7)
   'ACR', # Lot size
   'ACCESS', # Access to the Internet
   'TYPE', # Type of unit
   'RNTM', # Meals included in rent
   'BROADBND',
   'DIALUP',
   'DSL',
   'FIBEROP',
   'MODEM',
   'OTHSVCEX',
   'SATELLITE',
   'BUS', # Business or medical office on property
   'TEL',
   'BATH',
   'KIT',
   'PLM',
   'REFR',
   'RWAT', # Hot and cold running water
   'SINK',
   'STOV',
   'TOIL',

]

householdFeatures = [
   'NPF', # Number of persons in family
   'NP', # Number of person records following this housing record
   'NRC', # Number of related children in household
   'NOC', # Number of own children in household
   'WORKSTAT', # Work status of householder or spouse in family households
   'WKEXREL', # Work experience of householder and spouse
   'FES', # Family type and employment status (1-8)
   'MV', # When moved into this house or apartment (1-7)
   'HHT', # Household/family type,
   'AGS', # Sales of Agriculture Products (Yearly sales)
   'VEH', # Vehicles (1 ton or less) available
   'HHL', # Household language
   'SMX', # Second or junior mortgage or home equity loan status
   'FPARC', # Family presence and age of related children (1-4)
   'PARTNER', # Unmarried partner household
   'HUPAC', # HH presence and age of children
   'HUPAOC', # HH presence and age of own children
   'HUPARC', # HH presence and age of related children (1-4)
   'TEN', # Tenure (ownership of house)
   'WIF', # Workers in family during the past 12 months
   'MRGX', # First mortgage status
   'RESMODE', # Response mode
   'MRGI', # First mortgage payment includes fire/hazard/flood insurance
   'MRGT', # First mortgage payment includes real estate taxes
   'R60', # Presence of persons 60 years and over in household (0-2)
   'R65', # Presence of persons 65 years and over in household
   'SSMC', # Same-sex married couple households
   'COMPOTHX', # Other computer equipment
   'LNGI', # Limited English speaking households
   'MULTG', # Multigenerational Household
   'FS', # Food Stamps
   'HUGCL', # Household with grandparent living with grandchildren
   'NPP', # Grandparent headed household with no parent present
   'NR', # Presence of nonrelative in household
   'PSF', # Presence of subfamilies in Household
   'R18', # Presence of persons under 18 years in household
]

belongingsFeatures = [
   'HANDHELD',
   'LAPTOP',
]

