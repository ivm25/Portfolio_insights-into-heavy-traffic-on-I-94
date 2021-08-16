import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# Function definition and structures
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
    return fig, ax


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
    colormap = plt.cm.get_cmap('Dark2')
    if horizontalplot:
        plt.barh(df[s_1], df[s_2], color=colormap.colors)
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


# Data Exploration

metro_data = pd.read_csv("Metro_Interstate_Traffic_Volume.csv")
# Examining the first five rows
metro_data.head(5)
# Examining the last five rows
metro_data.tail(5)
metro_data.info()
metro_data['traffic_volume'].hist()
metro_data['traffic_volume'].describe()

# Tranforming the date_time column into datetime
metro_data["date_time"] = pd.to_datetime(metro_data["date_time"])
metro_data["hour"] = metro_data["date_time"].dt.hour
metro_data.info()


# Create day and night masks

day_mask = ((metro_data["hour"] >= 7) & (metro_data["hour"] <= 19))

night_mask = ((metro_data["hour"] >= 19) | (metro_data["hour"] <= 7))

day_traffic = metro_data[day_mask]

night_traffic = metro_data[night_mask]

# grid chart function call
grid_chart(day_traffic, night_traffic, s_2="traffic_volume",
           title_1="day_traffic", title_2="night_traffic",
           xlabel="traffic_volume",
           ylabel="counts",
           chart_type="hist",
           xlimit_top=7500,
           xlimit_bottom=0,
           ylimit_top=8500,
           ylimit_bottom=0)

night_traffic["traffic_volume"].describe()

day_traffic["traffic_volume"].describe()

# Feature Engineering
day_traffic['month'] = day_traffic['date_time'].dt.month
day_traffic['dayofweek'] = day_traffic['date_time'].dt.dayofweek
day_traffic['hour'] = day_traffic['date_time'].dt.hour
# 4 == Friday
bussiness_days = day_traffic.copy()[day_traffic['dayofweek'] <= 4]
# 5 == Saturday
weekend = day_traffic.copy()[day_traffic['dayofweek'] >= 5]
by_hour_business = groupings(bussiness_days, new_col='hour')
by_hour_weekend = groupings(weekend, new_col='hour')

# group the day_traffic data by month column and have a mean aggregate
group_by_month = groupings(day_traffic, new_col='month')

# create a line plot of the monthly grouped data
create_lineplot(group_by_month, s_1="month", s_2="traffic_volume",
                chart_title="day_traffic",
                x="month",
                y="traffic"
                )

# group the data by the day of week
by_dayofweek = groupings(day_traffic, new_col='dayofweek')

# visualise the traffic by day_of_week
create_lineplot(by_dayofweek, s_1="dayofweek", s_2="traffic_volume",
                chart_title="traffic_by_dayofweek",
                x="day_of_week",
                y="traffic")

grid_chart(by_hour_business,
           by_hour_weekend,
           s_1="hour",
           s_2="traffic_volume",
           title_1="business_days",
           title_2="weekends",
           xlabel="hour_of_day",
           ylabel="traffic",
           chart_type=None,
           xlimit_top=20,
           xlimit_bottom=5,
           ylimit_top=7000,
           ylimit_bottom=1500)

day_traffic[["traffic_volume", "temp", "rain_1h", "snow_1h",
             "clouds_all", "weather_main",
             "weather_description"]].corr()


create_scatterplot(day_traffic, s_1="temp", s_2="traffic_volume",
                   xlim_bottom=230)
by_weather_main = groupings(day_traffic, new_col="weather_main")
by_weather_description = groupings(day_traffic,
                                   new_col="weather_description")


create_barchart(by_weather_main, "weather_main", "traffic_volume",
                chart_title="traffic_by_weather_main",
                x="traffic_volume",
                y="weather_main",
                horizontalplot=True)

create_barchart(by_weather_description, "weather_description",
                "traffic_volume",
                chart_title="traffic_by_weather_description",
                x="traffic_volume",
                y="weather_main",
                horizontalplot=True)

if __name__ == "_main_":
    groupings()
