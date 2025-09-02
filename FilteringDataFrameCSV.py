import pandas as pd

brics = pd.read_csv('brics.csv', index_col=0)

is_huge = brics['area'] > 8 # we stored the filter condition of the dataset

print(brics[is_huge]) # DataSet[filter] - returns a filtered DataSet

print()

print(brics[brics['area'] > 8]) # we can just put filtering clause in square brackets; the result is a pandas Series