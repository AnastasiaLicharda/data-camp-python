import matplotlib.pyplot as plt
import pandas as pd

netflix_df = pd.read_csv('netflix_data.csv', index_col=0)

# Histograms:
# We can adjust the number of bars, or bins, using the "bins" argument.
# Increasing or decreasing this can give us a better idea of what the distribution looks like.

netflix_df['duration'].hist(bins=20)
plt.show()

# Bar plots:
# Bar plots can reveal relationships between a categorical variable and a numeric variable

# Here we are calculating mean of duration by genres
avg_duration_by_genre = netflix_df.groupby('genre')['duration'].mean()
print(avg_duration_by_genre)

# Visualize using a bar plot
avg_duration_by_genre.plot(kind='bar', title='Mean duration by genre')
plt.show()

# Line plots:
# Line plots are great for visualizing changes in numeric variables over time
# dataframe.plot(x='date', y='weight_kg', kind='line')
# plt.show()

# Scatter plots:
# Scatter plots are great for visualizing relationships between two numeric variables
# dataframe.plot(x='date', y='weight_kg', kind='scatter')
# plt.show()

netflix_df.plot(x='release_year', y='duration', kind='scatter')
plt.show()

# Layering plots:
# Plots can also be layered on top of one another
# We can use plt.legend(), passing in a list of labels, and then call show.
# We can also make the histograms translucent:
# by using hist's alpha= argument, which takes a number. 0 = completely transparent = invisible, and 1 = completely opaque.

netflix_df[netflix_df['genre'] == 'Action']['duration'].hist(alpha=0.7)
netflix_df[netflix_df['genre'] == 'Horror Movies']['duration'].hist(alpha=0.7)
plt.legend(['Action', 'Horror Movies'])
plt.show()