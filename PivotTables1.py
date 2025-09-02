import pandas as pd

netflix_df = pd.read_csv('netflix_data.csv', index_col=0)

# values= - the column that you want to summarize (get mean of this value), index= - the column that you want to group by
# by default, pivot_tables takes the mean value of each group
# to group by 2 variables, we can pass a second variable name into the columns= argument

netflix_df_pivot_table = netflix_df.pivot_table(values='duration', index='genre', columns='country')

print(netflix_df_pivot_table)

slicing_pivot_table = netflix_df_pivot_table.loc['Action':'Comedies']

print(slicing_pivot_table)