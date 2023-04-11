import numpy as np

print("A")

print("B")


def clean_df(df):
    df = df.dropna()

    return df

def remove_dub(df):
    df = df.drop_duplicates(subset=["name"])
    print("Drop just the name")
    return df