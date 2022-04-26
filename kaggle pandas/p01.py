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





