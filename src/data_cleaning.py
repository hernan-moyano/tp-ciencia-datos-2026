import pandas as pd


def load_data(filepath):
    """Load raw data from a CSV file."""
    return pd.read_csv(filepath)


def drop_duplicates(df):
    """Remove duplicate rows from a DataFrame."""
    return df.drop_duplicates()


def drop_missing(df, threshold=0.5):
    """Drop columns where the fraction of missing values exceeds threshold."""
    min_count = int((1 - threshold) * len(df))
    return df.dropna(axis=1, thresh=min_count)


def fill_missing(df, strategy="mean"):
    """Fill missing values using the given strategy ('mean', 'median', or 'mode')."""
    df = df.copy()
    for col in df.select_dtypes(include="number").columns:
        if strategy == "mean":
            df[col] = df[col].fillna(df[col].mean())
        elif strategy == "median":
            df[col] = df[col].fillna(df[col].median())
        elif strategy == "mode":
            df[col] = df[col].fillna(df[col].mode()[0])
    return df
