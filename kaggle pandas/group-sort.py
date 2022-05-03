import pandas as pd

melbourne_houses = pd.read_csv('./melb_data.csv')
col = melbourne_houses.groupby('Rooms')
# for i in col:
#     print(i)


melbourne_houses = pd.read_csv('./melb_data.csv')
col = melbourne_houses.groupby('Rooms').Price
# for i in col:
#     print(i)

melbourne_houses = pd.read_csv('./melb_data.csv')
col = melbourne_houses.loc[:,['Rooms']].groupby('Rooms')
# for i in col:
#     print(i)

melbourne_houses = pd.read_csv('./melb_data.csv')
col = melbourne_houses.loc[:,['Rooms','Price']].groupby('Rooms')
# for i in col:
#     print(i)

melbourne_houses = pd.read_csv('./melb_data.csv')
col = melbourne_houses.groupby('Rooms').Price.mean()


melbourne_houses = pd.read_csv('./melb_data.csv')
col = melbourne_houses.groupby('Rooms').Price.count()


melbourne_houses = pd.read_csv('./melb_data.csv')
col = melbourne_houses.count()


melbourne_houses = pd.read_csv('./melb_data.csv')
col = melbourne_houses.groupby(['Rooms','Suburb']).Price
# for i in col:
#     print(i)


melbourne_houses = pd.read_csv('./melb_data.csv')
col = melbourne_houses.groupby(['Rooms','Suburb']).Price
data = col.apply(lambda d: d.iloc[0])


melbourne_houses = pd.read_csv('./melb_data.csv')
col = melbourne_houses.groupby(['Rooms','Suburb']).Price.agg([len,min,max])


melbourne_houses = pd.read_csv('./melb_data.csv')
col = melbourne_houses.groupby(['Suburb','Rooms']).Price.agg([len,min,max])
print(col.sort_values(by='min'))