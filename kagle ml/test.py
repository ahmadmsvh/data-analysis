import pandas as pd

data = pd.read_csv('./melb_data.csv')

X_train = data.drop(['Price'], axis=1)
y_train = data['Price']



# s = (X_train.dtypes == 'object')
# for x in X_train:
#     print(x)

print(X_train.dtypes == 'object')

