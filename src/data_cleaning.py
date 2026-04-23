import pandas as pd
from typing import Union
from pathlib import Path

def load_data(filepath: Union[str, Path]) -> pd.DataFrame:
    """Load raw data from an Excel or CSV file."""
    filepath_str = str(filepath)
    if not filepath_str:
        raise ValueError("filepath cannot be empty")

    lower_path = filepath_str.lower()
    if lower_path.endswith((".xlsx", ".xls")):
        return pd.read_excel(filepath_str, sheet_name=0)  # pyright: ignore[reportUnknownMemberType]
    if lower_path.endswith(".csv"):
        return pd.read_csv(filepath_str)

    raise ValueError(
        "Unsupported file format. Use one of: .xlsx, .xls, .csv"
    )


def drop_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Remove duplicate rows from a DataFrame."""
    return df.drop_duplicates()


def drop_missing(df: pd.DataFrame, threshold: float = 0.5) -> pd.DataFrame:
    """Drop columns where the fraction of missing values exceeds threshold."""
    if not 0 <= threshold <= 1:
        raise ValueError("threshold must be between 0 and 1")

    min_count = int((1 - threshold) * len(df))
    return df.dropna(axis=1, thresh=min_count)


def fill_missing(df: pd.DataFrame, strategy: str = "mean") -> pd.DataFrame:
    """Fill missing values using the given strategy ('mean', 'median', or 'mode')."""
    if strategy not in {"mean", "median", "mode"}:
        raise ValueError("strategy must be one of: 'mean', 'median', 'mode'")

    df = df.copy()
    for col in df.select_dtypes(include="number").columns:
        if strategy == "mean":
            df[col] = df[col].fillna(df[col].mean())
        elif strategy == "median":
            df[col] = df[col].fillna(df[col].median())
        elif strategy == "mode":
            mode_series = df[col].mode(dropna=True)
            if not mode_series.empty:
                df[col] = df[col].fillna(mode_series.iloc[0])

    # For non-numeric columns, mode is the safest default fallback.
    for col in df.select_dtypes(exclude="number").columns:
        mode_series = df[col].mode(dropna=True)
        if not mode_series.empty:
            df[col] = df[col].fillna(mode_series.iloc[0])

    return df
