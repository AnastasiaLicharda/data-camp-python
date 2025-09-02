import pandas as pd

netflix_df = pd.read_csv('netflix_data.csv', index_col=0)

dramas_duration_mean = netflix_df[netflix_df['genre'] == 'Dramas']['duration'].mean() # We count the mean duration of the Dramas films
action_duration_mean = netflix_df[netflix_df['genre'] == 'Action']['duration'].mean() # We count the mean duration of the Action films

#print(dramas_duration_mean)
#print(action_duration_mean)

group_by_genre_duration_mean = netflix_df.groupby('genre')['duration'].mean()

group_by_genre_min_max_sum_duration = netflix_df.groupby('genre')['duration'].agg([min,max,sum])

#print(group_by_genre_duration_mean)
#print(group_by_genre_min_max_sum_duration)

group_by_genre_country_mean_duration = netflix_df.groupby(['genre','country'])['duration'].mean() # Grouping by multiple columns

print(group_by_genre_country_mean_duration)

# Group by multiple columns, aggregate by multiple columns
group_by_genre_country_mean_duration_year = netflix_df.groupby(['genre','country'])[['duration','release_year']].mean()

print(group_by_genre_country_mean_duration_year)