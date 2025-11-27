import matplotlib.pyplot as plt
import pandas as pd

netflix_df = pd.read_csv('netflix_data.csv', index_col=0)

# When we call isna() on a DataFrame,
# we get a Boolean for every single value indicating whether the value is missing or not,
# but this isn't very helpful when you're working with a lot of data.
print(netflix_df.isna())

# If we chain .isna() with .any(), we get one value for each variable that tells us if there are any missing values in that column.
print(netflix_df.isna().any())

# We can combine sum with isna() to count the number of NaNs in each column.
print(netflix_df.isna().sum())

# We can use those counts to visualize the missing values in the dataset using a bar plot.
netflix_df.isna().sum().plot(kind='bar')
plt.show()

# Removing missing values
# One option is to remove the rows in the DataFrame that contain missing values.
netflix_df.dropna()

# Replacing missing values
# Another option is to replace missing values with another value.
# The fillna() method takes in a value, and all NaNs will be replaced with this value.
netflix_df.fillna(0)