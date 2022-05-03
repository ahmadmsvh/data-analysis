import pandas as pd


melbourne_houses = pd.read_csv('./melb_data.csv')
type = melbourne_houses.dtypes


melbourne_houses = pd.read_csv('./melb_data.csv')
type = melbourne_houses.Price.dtype

# melbourne_houses.points.astype('float64')


melbourne_houses = pd.read_csv('./melb_data.csv')
col = melbourne_houses[pd.isnull(melbourne_houses.YearBuilt)].YearBuilt


melbourne_houses = pd.read_csv('./melb_data.csv')
col = melbourne_houses.YearBuilt.fillna(1900)
col = col.astype('int64')


melbourne_houses = pd.read_csv('./melb_data.csv')
col = melbourne_houses.Suburb.replace('Abbotsford','amadabad')
print(col)
