import pandas as pd

netflix_df = pd.read_csv('netflix_data.csv', index_col=0)

# Methods to do summary statistics:
# .mean(), .median(), .mode(),
# .min(), .max(),
# .var(), .std(),
# .sum(),
# .quantile()

# Cumulative statistics:
# .cumsum() - cumulative sum
# .cummax() - cumulative max
# .cummin() - cumulative min
# .cumprod() - cumulative product

duration_mean = netflix_df['duration'].mean() # The mean of a column
print(duration_mean)

duration_median = netflix_df['duration'].median() # The median of a column
print(duration_median)

duration_mode = netflix_df['duration'].mode() # The mode of a column
print(duration_mode)

duration_min = netflix_df['duration'].min() # The min of a column
print(duration_min)

duration_max = netflix_df['duration'].max() # The max of a column
print(duration_max)

# The .agg() method allows to compute custom summary statistics:

# Here we create a function that computes 30 percentile of a column
def pct30(column):
    return column.quantile(0.3)

def pct40(column):
    return column.quantile(0.4)

duration_30_pct = netflix_df['duration'].agg(pct30)
print(duration_30_pct)

print(netflix_df[['duration', 'release_year']].agg(pct30))

print(netflix_df['duration'].agg([pct30, pct40]))