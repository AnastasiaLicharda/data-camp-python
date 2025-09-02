import pandas as pd

brics = pd.read_csv("brics.csv", index_col = 0)

# Pandas Series
for lab, row in brics.iterrows():
    print(lab)
    print(row)

print()

# Selective print
for lab, row in brics.iterrows():
    print(lab + ": " + row["capital"])

print()

# Add column with a for loop (Pandas Series)
for lab, row in brics.iterrows():
    brics.loc[lab, "name_length"] = len(row["country"])
    print(brics)

print()

# Add column with apply() - DataFrame
brics["name_length"] = brics["country"].apply(len)
print(brics)