import pandas as pd
import matplotlib.pyplot as plt

# There are many ways to create DataFrames from scratch, but we'll discuss two ways:
# from a list of dictionaries - the DataFrame is built up row by row,
# and from a dictionary of lists - the DataFrame is built up column by column.

# List of dictionaries - by row
list_of_dicts = [{"name": "Ginger", "breed": "Dachshund", "height_cm": 22,"weight_kg": 10, "date_of_birth": "2019-03-14"},
                 {"name": "Scout", "breed": "Dalmatian", "height_cm": 59, "weight_kg": 25, "date_of_birth": "2019-05-09"}]

new_dogs1 = pd.DataFrame(list_of_dicts)
print(new_dogs1)

# Dictionary of lists - by column
dict_of_lists = {"name": ["Ginger", "Scout"],"breed": ["Dachshund", "Dalmatian"],"height_cm": [22, 59],
                 "weight_kg": [10, 25],"date_of_birth": ["2019-03-14", "2019-05-09"]}
new_dogs2 = pd.DataFrame(dict_of_lists)
print(new_dogs2)
