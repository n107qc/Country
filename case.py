import pandas as pd 
import matplotlib.pyplot as plt

#місце для твого коду
df = pd.read_csv("countries of the world.csv")
df.info()

def make_density(row1):
    if row1 != "0":
        return float(row1.replace(",","."))
    else: 
        return 0
df["Pop. Density (per sq. mi.)"]=df["Pop. Density (per sq. mi.)"].apply(make_density)
df.info()

def make_density(row2):
    if row2 != "0":
        return float(row2.replace(",","."))
    else: 
        return 0
df["Coastline (coast/area ratio)"]=df["Coastline (coast/area ratio)"].apply(make_density)
df.info()

def make_density(value):
    if isinstance(value, str):
        value = float(value.replace(",", "."))
    return value

df["Net migration"] = df["Net migration"].apply(make_density)
df.info()

def make_density(value):
    if isinstance(value, str):
        value = float(value.replace(",", "."))
    return value

df["Infant mortality (per 1000 births)"] = df["Infant mortality (per 1000 births)"].apply(make_density)
df.info()

def make_density(value):
    if isinstance(value, str):
        value = float(value.replace(",", "."))
    return value

df["Climate"] = df["Climate"].apply(make_density)
df.info()

def make_density(value):
    if isinstance(value, str):
        value = float(value.replace(",", "."))
    return value

df["Birthrate"] = df["Birthrate"].apply(make_density)
df.info()

def make_density(value):
    if isinstance(value, str):
        value = float(value.replace(",", "."))
    return value

df["Deathrate"] = df["Deathrate"].apply(make_density)
df.info()

def make_density(value):
    if isinstance(value, str):
        value = float(value.replace(",", "."))
    return value

df["Agriculture"] = df["Agriculture"].apply(make_density)
df.info()

def make_density(value):
    if isinstance(value, str):
        value = float(value.replace(",", "."))
    return value

df["Industry"] = df["Industry"].apply(make_density)
df.info()

def make_density(value):
    if isinstance(value, str):
        value = float(value.replace(",", "."))
    return value

df["Service"] = df["Service"].apply(make_density)
df.info()

def make_density(value):
    if isinstance(value, str):
        value = float(value.replace(",", "."))
    return value

df["Phones (per 1000)"] = df["Phones (per 1000)"].apply(make_density)
df.info()


def literacy(value):
    if isinstance(value, str):
        value = float(value.replace(",", "."))
    return value 

df['Literacy (%)'] = df['Literacy (%)'].apply(literacy)
df.info()

def literacy(value):
    if isinstance(value, str):
        value = float(value.replace(",", "."))
    return value 

df['Arable (%)'] = df['Arable (%)'].apply(literacy)
df.info()

def literacy(value):
    if isinstance(value, str):
        value = float(value.replace(",", "."))
    return value 

df['Crops (%)'] = df['Crops (%)'].apply(literacy)
df.info()

def literacy(value):
    if isinstance(value, str):
        value = float(value.replace(",", "."))
    return value 

df['Other (%)'] = df['Other (%)'].apply(literacy)
df.info()

df["Other (%)"].fillna(-1,inplace=True)
df.info()

df.to_csv('cleaned.csv')