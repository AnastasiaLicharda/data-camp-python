import pandas as pd

new_dogs = pd.read_csv('new_dogs.csv')

new_dogs["bmi"] = new_dogs["weight_kg"] / (new_dogs["height_cm"] / 100) ** 2

new_dogs.to_csv("new_dogs_with_bmi.csv")