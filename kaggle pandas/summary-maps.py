import pandas as pd

melbourne_houses = pd.read_csv("./melb_data.csv", index_col=1)
col = melbourne_houses.Price.describe()
print(col,'\n')



melbourne_houses = pd.read_csv("./melb_data.csv", index_col=0)
col = melbourne_houses.Address.describe()
# col = melbourne_houses.columns
print(col,'\n')


melbourne_houses = pd.read_csv("./melb_data.csv", index_col=1)
mean = melbourne_houses.Price.mean()
unique = melbourne_houses.Suburb.unique()
suburbcount = melbourne_houses.Suburb.value_counts()
print(mean,'\n')
print(unique,'\n')
print(suburbcount,'\n')

col = melbourne_houses.Price.map(lambda p: p - mean)
print(col,'\n')



melbourne_houses = pd.read_csv("./melb_data.csv")
melbourne_houses.AddressPlusSuburb = melbourne_houses.Address + ' - ' + melbourne_houses.Suburb
col = melbourne_houses.AddressPlusSuburb
print(col,'\n')