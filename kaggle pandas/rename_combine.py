import pandas as pd


melbourne_houses = pd.read_csv('./melb_data.csv')
col = melbourne_houses.iloc[0:10,1:4].rename(columns={'Address' : 'Location'})


melbourne_houses = pd.read_csv('./melb_data.csv')
col = melbourne_houses.iloc[0:10,1:4].rename(columns={'Address' : 'Location'})
col = col.rename(index={0 : 'zero', 1:'one'})
print(col)


# left = canadian_youtube.set_index(['title', 'trending_date'])
# right = british_youtube.set_index(['title', 'trending_date'])
# pd.concat([canadian_youtube, british_youtube])
# left.join(right, lsuffix='_CAN', rsuffix='_UK')