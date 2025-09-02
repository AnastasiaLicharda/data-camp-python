import pandas as pd

netflix_df = pd.read_csv('netflix_data.csv', index_col=0)

# .columns contains an Index object of column names in a dataframe
print(netflix_df.columns)

# .index contains an Index object of row numbers in a dataframe
print(netflix_df.index)

# Setting a column as the index
netflix_df_ind = netflix_df.set_index('title')
print(netflix_df_ind)

# Removing an index
# netflix_df_ind.reset_index()

# Dropping an index (remove this column from a dataframe)
# netflix_df_ind.reset_index(drop=True)


# Subsetting without using indexes
netflix_df_all_about = netflix_df[netflix_df['title'].isin(['All About Nina', 'All About Love'])]
print(netflix_df_all_about)

# Indexes make subsetting simpler (it's the same result but code is cleaner)
netflix_df_ind_all_about = netflix_df_ind.loc[['All About Nina', 'All About Love']]
print(netflix_df_ind_all_about)

# Multi-level indexes, or hierarchical indexes
# netflix_df_ind = netflix_df.set_index(['title', 'country'])

# Subset inner levels with a list of tuples
# netflix_df_ind.loc[[('All About Nina', 'United States'), ('All About Love', 'South Africa'),]]

# Controlling sort_index
# netflix_df_ind.sort_index(level=['title', 'country'], ascending=[True, False])

