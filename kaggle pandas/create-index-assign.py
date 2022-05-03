from numpy import isin
import pandas as pd 

a = pd.DataFrame({
    'Yes'   : [50,21],
    'No'    : [131,2]
})



a = pd.DataFrame({
    'yes'   : [50,21],
    'no'    : [131,2]
    },
    index=['question','answer']
)


a = pd.DataFrame({
    'Ali'   : [50,21],
    'John'    : [131,2]
    },
    index=['Yes','No']
)



b = pd.Series([1,2,'ali',1.23], index=['age','weight','name','index'],name='baby')

melbourne_houses = pd.read_csv("./melb_data.csv", index_col='Price')
melbourne_houses = pd.read_csv("./melb_data.csv", index_col=4)
shape = melbourne_houses.shape
describe = melbourne_houses.describe()
head = melbourne_houses.head()


cols = melbourne_houses.columns


melbourne_houses = pd.read_csv("./melb_data.csv", index_col=13)
col = melbourne_houses.Price



melbourne_houses = pd.read_csv("./melb_data.csv")
col = melbourne_houses.Price



melbourne_houses = pd.read_csv("./melb_data.csv", index_col=1)
col = melbourne_houses['Price']



melbourne_houses = pd.read_csv("./melb_data.csv", index_col=1)
rec = melbourne_houses['Price'][1]



melbourne_houses = pd.read_csv("./melb_data.csv", index_col=1)
rec = melbourne_houses.iloc[1:4]


melbourne_houses = pd.read_csv("./melb_data.csv", index_col=1)
col = melbourne_houses.iloc[1:4,2:5]


melbourne_houses = pd.read_csv("./melb_data.csv", index_col=1)
col = melbourne_houses.iloc[[1,3,76],[1,3,6]]



melbourne_houses = pd.read_csv("./melb_data.csv")
col = melbourne_houses.loc[[1,3,76],['Address','Price']]


melbourne_houses = pd.read_csv("./melb_data.csv",index_col=1)
col = melbourne_houses.loc['25 Bloomburg St':'49 Roberts Rd',['Price','Rooms']]


melbourne_houses = pd.read_csv("./melb_data.csv")
melbourne_houses.set_index('Rooms')
col = melbourne_houses.iloc[[1,3,76],[1,3,6]]


melbourne_houses = pd.read_csv("./melb_data.csv", index_col=1)
col = melbourne_houses['Rooms'] == 2


melbourne_houses = pd.read_csv("./melb_data.csv", index_col=1)
col = melbourne_houses.loc[(melbourne_houses['Rooms'] == 2) & (melbourne_houses['Price'] > 978000.0),['Rooms','Price']]


melbourne_houses = pd.read_csv("./melb_data.csv", index_col=1)
col = melbourne_houses.loc[melbourne_houses['Rooms'].isin([2,3]),['Rooms','Price']]


melbourne_houses = pd.read_csv("./melb_data.csv", index_col=1)
col = melbourne_houses.loc[melbourne_houses['Rooms'].notnull(),['Rooms','Price']]


melbourne_houses = pd.read_csv("./melb_data.csv", index_col=1)
col = melbourne_houses.loc[:,['Rooms','Price']]


melbourne_houses = pd.read_csv("./melb_data.csv", index_col=1)
melbourne_houses['BB'] = range(len(melbourne_houses),0,-1)
col = melbourne_houses.loc[:,['BB','Rooms','Price']]
print(col,'\n')
