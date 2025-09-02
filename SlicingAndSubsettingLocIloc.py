import pandas as pd

netflix_df = pd.read_csv('netflix_data.csv')

# You can only slice an index if the index is sorted (using .sort_index()).
# To slice at the outer level, first and last can be strings.
# To slice at inner levels, first and last should be tuples.
# If you pass a single slice to .loc[], it will slice the rows.
# .loc[] includes the last argument (1:4, 4 included), .iloc[] doesn't include the last argument (1:4, 4 not included)

netflix_df_sort = netflix_df.set_index(['country','genre']).sort_index()

print(netflix_df_sort)

slicing_df_outer = netflix_df_sort.loc['Argentina':'Canada']

print(slicing_df_outer)

# Slicing the inner index correctly (using tuples)
slicing_df_inner = netflix_df_sort.loc[('Argentina', 'Action'):('Canada', 'Comedies')]

print(slicing_df_inner)

slicing_columns = netflix_df_sort.loc[('Argentina', 'Action'):('Canada', 'Comedies'), 'title':'release_year']

print(slicing_columns)

# Subsetting by row/column numbers (using iloc)
print(netflix_df.iloc[:10, 1:6])