import pandas as pd


melbourne_houses = pd.read_csv('./melb_data.csv')
col = melbourne_houses.groupby('Rooms').Price
for i in col:
    print(i)


melbourne_houses = pd.read_csv('./melb_data.csv')
col = melbourne_houses.groupby('Rooms').Price.mean()
print(col,'\n')



melbourne_houses = pd.read_csv('./melb_data.csv')
col = melbourne_houses.count()
print(col,'\n')


melbourne_houses = pd.read_csv('./melb_data.csv')
col = melbourne_houses.groupby(['Rooms','Suburb']).Price
for i in col:
    print(i)


melbourne_houses = pd.read_csv('./melb_data.csv')
col = melbourne_houses.groupby(['Rooms','Suburb']).Price
data = col.apply(lambda d: d.iloc[0])
print(data)


melbourne_houses = pd.read_csv('./melb_data.csv')
col = melbourne_houses.groupby(['Rooms','Suburb']).Price.agg([len,min,max])
print(col,'\n')



melbourne_houses = pd.read_csv('./melb_data.csv')
col = melbourne_houses.groupby(['Suburb','Rooms']).Price.agg([len,min,max])
print(col.sort_values(by='min'))