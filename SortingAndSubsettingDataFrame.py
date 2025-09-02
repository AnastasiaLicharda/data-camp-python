import pandas as pd
import numpy as np

netflix_df = pd.read_csv('netflix_data.csv', index_col=0) # Pandas DataFrame from CSV

sort_values_asc = netflix_df.sort_values('duration') # Sort values by column in ASC order
#print(sort_values_asc)

sort_values_dsc = netflix_df.sort_values('duration', ascending=False) # Sort values by column is DSC order
#print(sort_values_dsc)

sort_values_multiple = netflix_df.sort_values(['title', 'duration']) # Sorting by multiple columns
#print(sort_values_multiple)

subset_column = netflix_df['duration'] # Subsetting one column of a dataset
#print(subset_column)

subset_multiple_columns = netflix_df[['title', 'duration']] # Subsetting multiple columns
#print(subset_multiple_columns)

# Creating filters for a dataset
short_duration_films = netflix_df['duration'] < 90
films_1990s = np.logical_and(netflix_df['release_year'] >= 1990, netflix_df['release_year'] < 2000)
action_films = netflix_df['genre'] == 'Action'

#print(netflix_df[short_duration_films & films_1990s & action_films]) # Subsetting based on multiple conditions (using & - 'logical and')

# Subsetting using .isin()
is_action_or_dramas = netflix_df['genre'].isin(['Action', 'Dramas'])
print(netflix_df[is_action_or_dramas])
