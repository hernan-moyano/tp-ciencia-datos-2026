import matplotlib.pyplot as plt
import seaborn as sns


def plot_distribution(df, column, save_path=None):
    """Plot the distribution of a numeric column."""
    fig, ax = plt.subplots()
    sns.histplot(df[column].dropna(), kde=True, ax=ax)
    ax.set_title(f"Distribution of {column}")
    ax.set_xlabel(column)
    ax.set_ylabel("Frequency")
    if save_path:
        fig.savefig(save_path)
    return fig


def plot_correlation_matrix(df, save_path=None):
    """Plot a heatmap of the correlation matrix for numeric columns."""
    fig, ax = plt.subplots(figsize=(10, 8))
    corr = df.select_dtypes(include="number").corr()
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
    ax.set_title("Correlation Matrix")
    if save_path:
        fig.savefig(save_path)
    return fig
