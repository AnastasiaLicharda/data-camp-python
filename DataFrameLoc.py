import pandas as pd

brics = pd.read_csv('brics.csv', index_col=0)

# [] - access columns or rows as Pandas Series, [[]] - access columns or rows as Pandas DataFrame
#print(brics['country']) - type = Series

#loc - label-based; access a group of rows and columns of a DataFrame by labels

#Pandas DataFrame, 1 row of a table
print(brics.loc[['RU']])

print()

#Pandas DataFrame, 3 rows of a table
print(brics.loc[['RU','IN','CH']])

print()

#Pandas DataFrame, select of 3 rows and 2 columns of a table
print(brics.loc[['RU','IN','CH'], ['country','capital']])

print()

#Pandas DataFrame, select of all rows and 2 columns of a table (: - all labels)
print(brics.loc[:, ['country','capital']])