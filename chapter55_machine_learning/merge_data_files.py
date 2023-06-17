import pandas as pd

# UK Gov Covid data downloaded on 20th Oct 2021
COVID_DATA = 'covid_data_overview_2021-10-20.csv'
# Data from the 19th Oct 2021 - only covers 2020 - so want to predict 2021 behaviour
MOBILITY_CHANGE = '2020_GB_Region_Mobility_Report_2021-10-19.csv'

# Load the UK Covid overview data
print(f'Loading - {COVID_DATA}')
df1 = pd.read_csv(COVID_DATA)

# Drop columns that don't provide any additional data
df1.drop(['areaCode',
          'areaName',
          'areaType',
          'newPeopleVaccinatedFirstDoseByPublishDate',
          'newPeopleVaccinatedSecondDoseByPublishDate'],
         axis='columns',
         inplace=True)
# Set the date column to be a datetime column
df1['date'] = pd.to_datetime(df1['date'])

# Sort the rows into ascending date order
df1.sort_values(by=["date"], ignore_index=True, inplace=True)

# Extract 2021 data for use in testing classifiers and save to file
date_mask_2021 = (df1['date'] >= '2021-01-01') & (df1['date'] <= '2021-12-31')
df_2021 = df1.loc[date_mask_2021]
df_2021.to_csv('covid_data_2021_only.csv', index=False)

# Want to select 2020-02-15 to the 2020-12-31 in terms of dates
# Set up a mask to indicate the date selection for 2020 and 2021
date_mask = (df1['date'] >= '2020-02-15') & (df1['date'] <= '2020-12-31')
# Select all the rows that meet the mask search criteria
df1 = df1.loc[date_mask]
# Replace missing values with zeros for hospitalCases
df1['hospitalCases'] = df1['hospitalCases'].fillna(0)
df1['newAdmissions'] = df1['newAdmissions'].fillna(0)

print(f'Loading - {MOBILITY_CHANGE}')

# Load the Google Mobility data for the UK
df2 = pd.read_csv(MOBILITY_CHANGE, low_memory=False)

# Drop columns that don't provide any additional data
df2.drop(['country_region_code',
          'country_region',
          'sub_region_1',
          'sub_region_2',
          'metro_area',
          'iso_3166_2_code',
          'census_fips_code',
          'place_id'],
         axis='columns',
         inplace=True)
df2['date'] = pd.to_datetime(df2['date'])
df2.rename(columns={'retail_and_recreation_percent_change_from_baseline': 'retail_and_recreation_change'}, inplace=True)
# Pick up the first 322 rows
df2 = df2.head(321)
# Can now concatenate them together into a single dateset
df3 = pd.merge(df1, df2, on='date')

print('Writing merged_covid_data.csv file')
df3.to_csv("merged_covid_data.csv", index=False)

