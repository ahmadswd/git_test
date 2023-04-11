import numpy as np

print("A")

print("B")


def clean_df(df):
    df = df.dropna()

    return df

def remove_dub(df):
    df = df.drop_duplicates(subset=["id"])
    print("drop by duplicates id")
    return df