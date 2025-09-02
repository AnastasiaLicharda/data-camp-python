import pandas as pd

netflix_df = pd.read_csv('netflix_data.csv', index_col=0)

# group_by_genre_duration_mean = netflix_df.groupby('genre')['duration'].mean()

# values= - the column that you want to summarize, index= - the column that you want to group by
# by default, pivot_tables takes the mean value of each group

mean_duration_by_genre = netflix_df.pivot_table(values='duration',index='genre')

print(mean_duration_by_genre)

# use aggfunc= to pass it a function (if we need a different summary statistics)
median_duration_by_genre = netflix_df.pivot_table(values='duration',index='genre',aggfunc=['median','mean'])

print(median_duration_by_genre)

# group_by_genre_country_mean_duration = netflix_df.groupby(['genre','country'])['duration'].mean() - Grouping by multiple columns

# to group by 2 variables, we can pass a second variable name into the columns=

# fill_value= - replaces NaN

# margins=True - the last row and the last column of the pivot table will contain the mean of all values in the column or row
# (not including the missing values)

mean_duration_by_genre_country = netflix_df.pivot_table(values='duration',index='genre',columns='country',fill_value=0,margins=True)

print(mean_duration_by_genre_country)