import os

import matplotlib.pyplot as plt
import seaborn as sns

from utils import ensure_dir


def plot_distribution(df, column, save_path=None):
    """Plot the distribution of a numeric column."""
    if column not in df.columns:
        raise ValueError(f"Column '{column}' does not exist in DataFrame")

    if df[column].dropna().empty:
        raise ValueError(f"Column '{column}' has no non-null values to plot")

    fig, ax = plt.subplots()
    sns.histplot(df[column].dropna(), kde=True, ax=ax)
    ax.set_title(f"Distribution of {column}")
    ax.set_xlabel(column)
    ax.set_ylabel("Frequency")
    if save_path:
        output_dir = os.path.dirname(str(save_path)) or "."
        ensure_dir(output_dir)
        fig.savefig(save_path)
    return fig


def plot_correlation_matrix(df, save_path=None):
    """Plot a heatmap of the correlation matrix for numeric columns."""
    numeric_df = df.select_dtypes(include="number")
    if numeric_df.shape[1] < 2:
        raise ValueError("At least two numeric columns are required to compute correlation matrix")

    fig, ax = plt.subplots(figsize=(10, 8))
    corr = numeric_df.corr()
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
    ax.set_title("Correlation Matrix")
    if save_path:
        output_dir = os.path.dirname(str(save_path)) or "."
        ensure_dir(output_dir)
        fig.savefig(save_path)
    return fig
