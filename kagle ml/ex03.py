import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer



# Read the data
X = pd.read_csv('./train.csv', index_col='Id') 
X_test = pd.read_csv('./test.csv', index_col='Id')
print(X_test.shape)

# Remove rows with missing target, separate target from predictors
X.dropna(axis=0, subset=['SalePrice'], inplace=True)

y = X.SalePrice
X.drop(['SalePrice'], axis=1, inplace=True)

# To keep things simple, we'll drop columns with missing values
cols_with_missing = [col for col in X.columns if X[col].isnull().any()] 

X.drop(cols_with_missing, axis=1, inplace=True)
X_test.drop(cols_with_missing, axis=1, inplace=True)
# Break off validation set from training data
X_train, X_valid, y_train, y_valid = train_test_split(X, y,train_size=0.8, test_size=0.2,random_state=0)


def score_dataset(X_train, X_valid, y_train, y_valid):
    model = RandomForestRegressor(n_estimators=100, random_state=0)
    model.fit(X_train, y_train)
    preds = model.predict(X_valid)
    return mean_absolute_error(y_valid, preds)


# Categorical columns in the training data
object_cols = [col for col in X_train.columns if X_train[col].dtype == "object"]

# Columns that can be safely ordinal encoded
good_label_cols = [col for col in object_cols if 
                   set(X_valid[col]).issubset(set(X_train[col]))]
        
# Problematic columns that will be dropped from the dataset
bad_label_cols = list(set(object_cols) - set(good_label_cols))
        
print('Categorical columns that will be ordinal encoded:', good_label_cols)
print('\nCategorical columns that will be dropped from the dataset:', bad_label_cols)



# Drop categorical columns that will not be encoded
label_X_train = X_train.drop(bad_label_cols, axis=1)
label_X_valid = X_valid.drop(bad_label_cols, axis=1)
label_X_test = X_test.drop(bad_label_cols, axis=1)

# Apply ordinal encoder 
 # Your code here
ordinal_encoder = OrdinalEncoder()
label_X_train[good_label_cols] = ordinal_encoder.fit_transform(X_train[good_label_cols])
label_X_valid[good_label_cols] = ordinal_encoder.transform(X_valid[good_label_cols])
label_X_test[good_label_cols] = ordinal_encoder.fit_transform(X_test[good_label_cols])




## Get number of unique entries in each column with categorical data

object_nunique = list(map(lambda col: X_train[col].nunique(), object_cols))
d = dict(zip(object_cols, object_nunique))
# Print number of unique entries by column, in ascending order
sorted(d.items(), key=lambda x: x[1])



# Columns that will be one-hot encoded
low_cardinality_cols = [col for col in object_cols if X_train[col].nunique() < 10]

# Columns that will be dropped from the dataset
high_cardinality_cols = list(set(object_cols)-set(low_cardinality_cols))

print('Categorical columns that will be one-hot encoded:', low_cardinality_cols)
print('\nCategorical columns that will be dropped from the dataset:', high_cardinality_cols)



# Use as many lines of code as you need!
model = OneHotEncoder(handle_unknown='ignore', sparse=False)
OH_cols_train = pd.DataFrame(model.fit_transform(X_train[low_cardinality_cols]))
OH_cols_valid = pd.DataFrame(model.transform(X_valid[low_cardinality_cols]))
OH_cols_test = pd.DataFrame(model.transform(X_test[low_cardinality_cols]))


OH_cols_train.index = X_train.index
OH_cols_valid.index = X_valid.index
OH_cols_test.index = X_test.index


num_cols_train = X_train.drop(object_cols, axis=1)
num_cols_valid = X_valid.drop(object_cols, axis=1)
num_cols_test = X_test.drop(object_cols, axis=1)

OH_X_train = pd.concat([num_cols_train , OH_cols_train], axis=1) # Your code here
OH_X_valid = pd.concat([num_cols_valid , OH_cols_valid], axis=1) # Your code here
OH_X_test = pd.concat([num_cols_test , OH_cols_test], axis=1)    # Your code here

OH_X_train.columns = list(map(lambda col: str(col),OH_X_train.columns))
OH_X_valid.columns = list(map(lambda col: str(col),OH_X_valid.columns))
OH_X_test.columns = list(map(lambda col: str(col),OH_X_test.columns))

my_imputer = SimpleImputer()
imputed_X_test = pd.DataFrame(my_imputer.fit_transform(OH_X_test))

# Imputation removed column names; put them back
imputed_X_test.columns = OH_X_test.columns


print("MAE from Approach 3 (One-Hot Encoding):") 
print(score_dataset(OH_X_train, OH_X_valid, y_train, y_valid))


my_model = RandomForestRegressor(n_estimators=100, criterion='absolute_error', random_state=0) 

my_model.fit(OH_X_train, y_train)

preds_test = my_model.predict(imputed_X_test)