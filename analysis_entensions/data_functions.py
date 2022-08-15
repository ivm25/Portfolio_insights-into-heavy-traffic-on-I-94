# Imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np




def groupings(df, new_col=None):
    """Group the input dataframe by a chosen column using a mean aggregation.

    df (DataFrame): input dataframe
    new_col (Series): chosen column for aggregation
    Returns_:
    grouped_df: DataFrame
    """
    grouped_df = df.groupby(new_col).mean()
    grouped_df = grouped_df.reset_index()
    return grouped_df

