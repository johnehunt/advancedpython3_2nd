import pickle
import pandas as pd
from matplotlib import pyplot as plt

CLASSIFIER_FILE = 'random_forest_regressor.pkl'

file = open(CLASSIFIER_FILE, "br")
regressor = pickle.load(file)

COVID_2021_DATA_FILE = 'covid_data_2021_only.csv'

# load data file
print(f'Loading - {COVID_2021_DATA_FILE}')

# Process the data so that it matches the classifiers requirements
df = pd.read_csv(COVID_2021_DATA_FILE)
df.sort_values(by=["date"], ignore_index=True, inplace=True)
# Store date column for use with output
dates = df['date']

# Drop date as now used in classifier
df.drop(['date'], axis='columns', inplace=True)

# Make sure all columns have a value even if its Zero
df['hospitalCases'] = df['hospitalCases'].fillna(0)
df['newAdmissions'] = df['newAdmissions'].fillna(0)
df['newCasesByPublishDate'] = df['newCasesByPublishDate'].fillna(0)

# Process the data and predict results
predictions = regressor.predict(df)

# Print out predictions for each date
# for i in range(len(dates)):
#     print(f'For {dates[i]} the predicted result is {results[i]}')

# Need to display graph with two axis

df['date'] = dates
df.set_index('date')
# Add second subplot
predicted_results_df = pd.DataFrame(index=dates, data=predictions, columns=["percent_change"])

fig, axes = plt.subplots(nrows=2, ncols=1)

df.plot(ax=axes[0])
predicted_results_df.plot(ax=axes[1])

plt.show()
