import pandas as pd

taxi_owners = pd.read_csv('taxi_owners.csv')
taxi_veh = pd.read_csv('taxi_veh2.csv')

taxi_own_veh = taxi_owners.merge(taxi_veh, on='vid', how='left')
print(taxi_own_veh)
