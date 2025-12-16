import pandas as pd

taxi_owners = pd.read_csv('taxi_owners.csv')
taxi_veh = pd.read_csv('taxi_veh.csv')

# Merge two DataFrames together with the .merge() method
taxi_own_veh = taxi_owners.merge(taxi_veh, on='vid', suffixes=('_own', '_veh'))

print(taxi_own_veh)

# Print rows and columns
print(taxi_own_veh.shape)

# Print the value_counts to find the most popular fuel_type
print(taxi_own_veh['fuel_type'].value_counts())
