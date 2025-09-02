import pandas as pd

netflix_df = pd.read_csv('netflix_data.csv', index_col=0) # Pandas DataFrame from CSV

head = netflix_df.head() # Head of a DataFrame (first 5 rows)
#print(head)

#netflix_df.info() # Info of a DataFrame (types of columns, non-nulls etc)

shape = netflix_df.shape # Count of columns and rows in a DataFrame
#print(shape)

describe = netflix_df.describe() # Some summary statistics for numerical columns
#print(describe)

values = netflix_df.values # The values attribute contains the data values in a 2D NumPy array
#print(values)

columns = netflix_df.columns # The columns attribute contains the data columns / labels in an array
#print(columns)

index = netflix_df.index # The index attribute contains row numbers or row names
#print(index)

# Shape, values, columns and index are attributes