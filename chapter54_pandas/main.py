import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

df1 = pd.read_csv('overview_2021-07-15.csv')

# print(df1.head().to_string())
# print(df1.tail().to_string())

df1.drop(['areaCode', 'areaName', 'areaType'],
         axis='columns',
         inplace=True)
# print(df1.head().to_string())

df1['date'] = pd.to_datetime(df1['date'])

# Sort the rows into ascending date order
df1.sort_values(by=["date"],
                ignore_index=True,
                inplace=True)
# Want to select 2020-02-15 to 2020-12-31 dates
# Set up a mask to indicate the date election
date_mask = (df1['date'] > '2020-02-14') & (df1['date'] <= '2020-12-31')
# Select all the rows that meet the mask search criteria
df1 = df1.loc[date_mask]

# print(df1.head().to_string())
# print(df1.tail().to_string())

is_null_count = df1.isnull().sum()
# print(is_null_count)

df1.drop(['newPeopleVaccinatedFirstDoseByPublishDate',
          'newPeopleVaccinatedSecondDoseByPublishDate'],
         axis='columns',
         inplace=True)

# Select a random sample of 10 rows form the DataFrame
# print(df1.sample(10).to_string())

# Load the google Mobility data for the UK
df2 = pd.read_csv('2020_GB_Region_Mobility_Report.csv', low_memory=False)

# Drop columns that don;t provide any additional data
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

# print(df2.sample(10).to_string())

df3 = pd.merge(df1, df2, on='date')
# print(df3.sample(10).to_string())

# print(df3.corr().to_string())

# Lets compare the hospital cases against retail and recreation change
# df4 = pd.concat([df3['date'],
#                  df3['hospitalCases'],
#                  df3['retail_and_recreation_change']], axis=1)
#
# axis1 = df4.plot(x="date", y="hospitalCases", legend=False)
# axis2 = axis1.twinx()
# df4.plot(x="date",
#          y="retail_and_recreation_change",
#          ax=axis2,
#          legend=False,
#          color="r")
# axis1.figure.legend()


df5 = pd.concat([df3['date'],
                 df3['hospitalCases'].rolling(7).mean(),
                 df3['retail_and_recreation_change'].rolling(7).mean()], axis=1)
ax1 = df5.plot(x="date", y="hospitalCases", legend=False, color="b")
ax2 = ax1.twinx()
df5.plot(x="date",
         y="retail_and_recreation_change",
         ax=ax2,
         legend=False,
         color="r")
ax1.set_ylabel('cases', color='b')
ax2.set_ylabel('% change from baseline', color='r')

ax1.figure.legend()

plt.show()

