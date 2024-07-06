import pandas as pd
#місце для твого коду
df = pd.read_csv("countries of the world.csv")
df.info()

def make_density(row):
    if row != "0":
        return float(row.replace(",","."))
    else: 
        return 0
df["Pop. Density (per sq. mi.)"]=df["Pop. Density (per sq. mi.)"].apply(make_density)
df.info()