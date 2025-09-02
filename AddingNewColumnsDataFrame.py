import pandas as pd

netflix_df = pd.read_csv('netflix_data.csv', index_col=0) # Pandas DataFrame from CSV

netflix_df['is_short_film'] = netflix_df['duration'] < 90
print(netflix_df[['duration', 'is_short_film']])