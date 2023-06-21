import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor

DATA_SET = 'merged_covid_data.csv'
TARGET_VARIABLE = 'retail_and_recreation_change'
FEATURES_LIST = ['hospitalCases', 'newAdmissions', 'newCasesByPublishDate']


def run_model(label,
              model,
              training_feature_set,
              training_target_attribute,
              test_feature_set,
              test_target_attribute):
    model.fit(training_feature_set, training_target_attribute)

    # Determine the metrics - against the training data
    pred_train_rf = model.predict(training_feature_set)
    trainingRMSE = np.sqrt(mean_squared_error(training_target_attribute, pred_train_rf))
    trainingRSquared = r2_score(training_target_attribute, pred_train_rf)
    trainingRSquared *= 100

    # Determine the metrics based on the test dataset
    pred_test = model.predict(test_feature_set)
    testingRMSE = np.sqrt(mean_squared_error(test_target_attribute, pred_test))
    testingRSquared = r2_score(test_target_attribute, pred_test)
    testingRSquared *= 100

    print(f'Testing {label} against Training data')
    print(f'Training RMSE - {trainingRMSE:.1f}')
    print(f'Training R-squared - {trainingRSquared:.1f}%')

    print(f'Testing {label} against test data')
    print(f'Testing RMSE - {testingRMSE:.1f}')
    print(f'Testing R-squared - {testingRSquared:.1f}%')


def print_menu(title, options, prompt):
    while True:
        print(title)
        length_of_options = len(options)
        for row in range(length_of_options):
            print(f'\t{row + 1} {options[row]}')
        user_option = input(prompt)
        if not user_option.isnumeric():
            print('Input must be a number')
        else:
            user_option = int(user_option)
            if user_option < 0 or user_option > length_of_options:
                print(f'Selection must be in the range 1 to {length_of_options}')
            else:
                break
    return user_option


def save_classifier(regressor):
    import pickle

    input_yes_no = input(f'Do you want to save the classifier for later use? ')
    if input_yes_no.lower() == 'y':
        filename = input("Please input the name for the classifier file: ")
        if not filename.endswith('.pkl'):
            filename += '.pkl'
        # Save the classifier:
        file = open(filename, "bw")
        pickle.dump(regressor, file)


print(f'Loading - {DATA_SET}')
# Load the merged data set
df = pd.read_csv(DATA_SET)

print('-' * 25)

print('Partition the Data - into train and test')

print('training data 80%, test data 20%')
train, test = train_test_split(df, test_size=0.2)
print(f'Size of training data {len(train)}')
print(f'Size of testing data {len(test)}')

training_features = train[FEATURES_LIST].values
training_target = train[TARGET_VARIABLE].values

test_features = test[FEATURES_LIST].values
test_target = test[TARGET_VARIABLE].values

print('-' * 25)

model = None

option = print_menu('Classifier Selection Menu',
                    ['KNN',
                     'Decision Tree',
                     'Random Forest'],
                    'Please select an option: ')

if option == 1:
    print('Build a KNN Classifier')
    print('=' * 20)
    # Use n nearest neighbors to predict the value of a future data point
    print(f'KNeighborsRegressor(n_neighbors=3)')
    model = KNeighborsRegressor(n_neighbors=3)
    run_model('KNN', model, training_features, training_target, test_features, test_target)

elif option == 2:
    print('Build a Decision Tree')
    print('=' * 20)
    MAX_DEPTH = 4
    print(f'DecisionTreeRegressor(max_depth={MAX_DEPTH}, min_samples_leaf=0.13, random_state=3)')
    model = DecisionTreeRegressor(max_depth=MAX_DEPTH, min_samples_leaf=0.13, random_state=3)
    run_model('Decision Tree', model, training_features, training_target, test_features,
              test_target)

elif option == 3:
    print('Build a Random Forest')
    print('=' * 20)
    # You could explore additional settings for Random Forest
    SIZE_OF_FOREST = 500
    print(f'RandomForestRegressor(max_depth=4, n_estimators={SIZE_OF_FOREST})')
    model = RandomForestRegressor(max_depth=4, n_estimators=SIZE_OF_FOREST)
    run_model('Random Forest', model, training_features, training_target, test_features,
              test_target)

save_classifier(model)

print('Done')
