import pandas as pd

brics = pd.read_csv('brics.csv', index_col=0)

#print(brics[['country']]) - DataFrame, 1 column of a table
#print(brics[['country','capital']]) - DataFrame, 2 columns of a table

print(brics)