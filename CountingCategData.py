import pandas as pd

netflix_df = pd.read_csv('netflix_data.csv', index_col=0)

distinct_genres = netflix_df.drop_duplicates(subset='genre') # .drop_duplicates(subset='') - takes distinct values from a column (subset=column)
print(distinct_genres)

count_of_genres = netflix_df['genre'].value_counts() # .values_counts() - counts values from a column

count_of_years = netflix_df['release_year'].value_counts(sort=True) # the argument sort=True - the biggest values are showing first

#print(count_of_years)

# The normalize argument can be used to turn the counts into proportions of the total
count_of_years_normalized = netflix_df['release_year'].value_counts(normalize=True)
print(count_of_years_normalized)