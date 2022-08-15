#Imports

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np





def grid_chart(df_1,
               df_2,
               s_1=None,
               s_2=None,
               title_1=None,
               title_2=None,
               xlabel=None,
               ylabel=None,
               chart_type=None,
               xlimit_top=None,
               xlimit_bottom=None,
               ylimit_top=None,
               ylimit_bottom=None
               ):
    """Plot a grid chart of an input dataFrame.

    df_1 (DataFrame): input dataframe 1
    df_2 (DataFrame): input dataframe 2
    s_1 (Series): chosen column as x-axis for the gridcharts
    s_2 (Series): chosen column as y-axis for the gridcharts
    title_1 (string): title of 1st grid chart
    title_2 (string): title of 2nd grid chart
    xlabel (string): label of x axes of grid charts
    ylabel (string): label of y axes of grid charts
    chart_type (type of chart): plots a histogram if value set
    to 'hist' else plots a lineplot
    xlim_bottom (int): start value of x axis
    xlim_top (int): right limit of x axis
    ylim_bottom (int): top limit of y axis
    ylim_top (int): start of y axis
    Returns_:
    gridchart(histogram/lineplot) (figure) with two axes: matplotlib figure
    """
    fig, ax = plt.subplots(nrows=1, ncols=2)
    plt.subplots_adjust(wspace=0.4)
    if chart_type == "hist":
        ax[0].hist(df_1[s_2])
        ax[1].hist(df_2[s_2])
    else:
        ax[0].plot(df_1[s_1], df_1[s_2])
        ax[1].plot(df_2[s_1], df_2[s_2])
    ax[0].set_title(title_1)
    ax[0].set_xlabel(xlabel)
    ax[0].set_xlim(xlimit_bottom,  xlimit_top)
    ax[0].set_ylabel(ylabel)
    ax[0].set_ylim(ylimit_bottom, ylimit_top)
    ax[1].set_title(title_2)
    ax[1].set_xlabel(xlabel)
    ax[1].set_xlim(xlimit_bottom, xlimit_top)
    ax[1].set_ylabel(ylabel)
    ax[1].set_ylim(ylimit_bottom, ylimit_top)
    plt.show()
    return fig, ax



# Generate line plots
def create_lineplot(df, s_1=None,
                    s_2=None,
                    chart_title=None,
                    x=None,
                    y=None,
                    ):
    """Plot a lineplot of an input dataFrame.

    df (DataFrame): input dataframe
    s_1 (Series): chosen column as x-axis for lineplot
    s_2 (Series): chosen column as y-axis for lineplot
    chart_title (String): title of the lineplot
    x (string): label of the x-axis
    y (string): label of the y-axis
    Returns_:
    lineplot (figure) and axis: matplotlib figure
    """
    if type(df) != pd.DataFrame:
        print("Please provide a pandas Dataframe as input")
        
        
    fig, ax = plt.subplots()
    plt.plot(df[s_1], df[s_2])
    plt.title(chart_title)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.show()
    return fig, ax


def create_scatterplot(df, s_1=None,
                       s_2=None,
                       xlim_bottom=None,
                       xlim_top=None,
                       ylim_bottom=None,
                       ylim_top=None
                       ):
    """Plot a scatterplot of an input dataFrame.

    df (DataFrame): input dataframe
    s_1 (Series): chosen column as x-axis for lineplot
    s_2 (Series): chosen column as y-axis for lineplot
    xlim_bottom (int): start value of x axis
    xlim_top (int): right limit of x axis
    ylim_bottom (int): top limit of y axis
    ylim_top (int): start of y axis
    Returns_:
    scatterplot (figure) and axis: matplotlib figure
    """
    fig, ax = plt.subplots()
    plt.scatter(df[s_1], df[s_2])
    ax.set_xlim(xlim_bottom, xlim_top)
    ax.set_ylim(ylim_bottom, ylim_top)
    plt.show()
    return fig, ax


def create_barchart(df, s_1=None,
                    s_2=None,
                    chart_title=None,
                    x=None,
                    y=None,
                    horizontalplot=False):
    """Plot a barchart of an input dataFrame.

    df (DataFrame): input dataframe
    s_1 (Series): chosen column as x-axis for lineplot
    s_2 (Series): chosen column as y-axis for lineplot
    chart_title (String): Title of the bar plot
    x (String): Label of x-axis
    y (String): Label of y-axis
    horizontalplot (boolean): plots a horizonatal bar plot if True
    Returns_:
    barchart (figure) and axis: matplotlib figure
    """
    fig, ax = plt.subplots(figsize=(8, 6))
    colormap = plt.cm.get_cmap('tab20c')
    if horizontalplot:
        plt.barh(df[s_1], df[s_2], color = colormap.colors)
        plt.title(chart_title)
        plt.xlabel(x)
        plt.ylabel(y)
        plt.show()
    else:
        plt.bar(df[s_1], df[s_2])
        plt.title(chart_title)
        plt.xlabel(x)
        plt.ylabel(y)
        plt.show()
    return fig, ax