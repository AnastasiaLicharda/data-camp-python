import pandas as pd
import numpy as np

brics = pd.read_csv('brics.csv', index_col=0)

filter_and = np.logical_and(brics['area'] > 8, brics['area'] < 10)

print(brics[filter_and])

print()

print(brics[np.logical_and(brics['area'] > 8, brics['area'] < 10)])