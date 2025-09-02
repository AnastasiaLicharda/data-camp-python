import pandas as pd

brics = pd.read_csv('brics.csv', index_col=0)

# [] - access columns or rows as Pandas Series, [[]] - access columns or rows as Pandas DataFrame
# brics['country'] : type = Series

#iloc - index-based; integer-location based indexing for selection by position.

#Pandas DataFrame, 1 row of a table
print(brics.iloc[[1]])

print()

#Pandas DataFrame, 3 rows of a table
print(brics.iloc[[1,2,3]])

print()

#Pandas DataFrame, select of 3 rows and 2 columns of a table
print(brics.iloc[[1,2,3], [0,1]])

print()

#Pandas DataFrame, select of all rows and 2 columns of a table (: - all labels)
print(brics.iloc[:, [0,1]])