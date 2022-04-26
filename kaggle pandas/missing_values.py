import pandas as pd


melbourne_houses = pd.read_csv('./melb_data.csv')
type = melbourne_houses.dtypes
print(type)




melbourne_houses = pd.read_csv('./melb_data.csv')
type = melbourne_houses.Price.dtype
print(type)

# reviews.points.astype('float64')


melbourne_houses = pd.read_csv('./melb_data.csv')
col = melbourne_houses[pd.isnull(melbourne_houses.YearBuilt)].YearBuilt
print(col)


melbourne_houses = pd.read_csv('./melb_data.csv')
col = melbourne_houses.YearBuilt.fillna(1900)
col = col.astype('int64')
print(col)


melbourne_houses = pd.read_csv('./melb_data.csv')
col = melbourne_houses.Suburb.replace('Abbotsford','amadabad')
print(col)