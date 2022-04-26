from numpy import isin
import pandas as pd 

a = pd.DataFrame({
    'Yes'   : [50,21],
    'No'    : [131,2]
})
print(a,'\n')


a = pd.DataFrame({
    'yes'   : [50,21],
    'no'    : [131,2]
    },
    index=['question','answer']
)
print(a,'\n')

a = pd.DataFrame({
    'Ali'   : [50,21],
    'John'    : [131,2]
    },
    index=['Yes','No']
)
print(a,'\n')


b = pd.Series([1,2,'ali',1.23], index=['age','weight','name','index'],name='baby')
print(b,'\n')


melbourne_houses = pd.read_csv("./melb_data.csv", index_col=1)
describe = melbourne_houses.describe()
shape = melbourne_houses.shape
head = melbourne_houses.head()

print(head,'\n')


cols = melbourne_houses.columns
print(cols,'\n')


melbourne_houses = pd.read_csv("./melb_data.csv", index_col=1)
col = melbourne_houses.Price
print(col,'\n')


melbourne_houses = pd.read_csv("./melb_data.csv")
col = melbourne_houses.Price
print(col,'\n')


melbourne_houses = pd.read_csv("./melb_data.csv", index_col=1)
col = melbourne_houses['Price']
print(col,'\n')


melbourne_houses = pd.read_csv("./melb_data.csv", index_col=1)
col = melbourne_houses['Price'][1]
print(col,'\n')


melbourne_houses = pd.read_csv("./melb_data.csv", index_col=1)
col = melbourne_houses.iloc[1:4]
print(col,'\n')


melbourne_houses = pd.read_csv("./melb_data.csv", index_col=1)
col = melbourne_houses.iloc[1:4,2:5]
print(col,'\n')


melbourne_houses = pd.read_csv("./melb_data.csv", index_col=1)
col = melbourne_houses.iloc[[1,3,76],[1,3,6]]
print(col,'\n')


melbourne_houses = pd.read_csv("./melb_data.csv")
col = melbourne_houses.loc[[1,3,76],['Address','Price']]
print(col,'\n')


melbourne_houses = pd.read_csv("./melb_data.csv",index_col=1)
col = melbourne_houses.loc['25 Bloomburg St':'49 Roberts Rd',['Price','Rooms']]
print(col,'\n')


melbourne_houses = pd.read_csv("./melb_data.csv")
melbourne_houses.set_index('Rooms')
col = melbourne_houses.iloc[[1,3,76],[1,3,6]]
print(col,'\n')



melbourne_houses = pd.read_csv("./melb_data.csv", index_col=1)
col = melbourne_houses['Rooms'] == 2
print(col,'\n')


melbourne_houses = pd.read_csv("./melb_data.csv", index_col=1)
col = melbourne_houses.loc[(melbourne_houses['Rooms'] == 2) & (melbourne_houses['Price'] > 978000.0),['Rooms','Price']]
print(col,'\n')


melbourne_houses = pd.read_csv("./melb_data.csv", index_col=1)
col = melbourne_houses.loc[melbourne_houses['Rooms'].isin([2,3]),['Rooms','Price']]
print(col,'\n')


melbourne_houses = pd.read_csv("./melb_data.csv", index_col=1)
col = melbourne_houses.loc[melbourne_houses['Rooms'].notnull(),['Rooms','Price']]
print(col,'\n')


melbourne_houses = pd.read_csv("./melb_data.csv", index_col=1)
col = melbourne_houses.loc[:,['Rooms','Price']]
print(col,'\n')


melbourne_houses = pd.read_csv("./melb_data.csv", index_col=1)
melbourne_houses['BB'] = range(len(melbourne_houses),0,-1)
col = melbourne_houses.loc[:,['BB','Rooms','Price']]
print(col,'\n')