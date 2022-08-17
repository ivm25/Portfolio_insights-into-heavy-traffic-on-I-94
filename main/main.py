import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

from analysis_entensions.charts import *
from analysis_entensions.data_functions import *



if __name__ == "_main_":
        
    metro_data = pd.read_csv("Metro_Interstate_Traffic_Volume.csv")
  
    # Tranforming the date_time column into datetime
    metro_data["date_time"] = pd.to_datetime(metro_data["date_time"])
    metro_data["hour"] = metro_data["date_time"].dt.hour
    metro_data.info()


    # Create day and night masks
    day_mask = ((metro_data["hour"] >= 7) & (metro_data["hour"] <= 19))

    night_mask = ((metro_data["hour"] >= 19) | (metro_data["hour"] <= 7))

    day_traffic = metro_data[day_mask]

    night_traffic = metro_data[night_mask]
    

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
    
    # group the data by the day of week
    by_dayofweek = groupings(day_traffic, 
                             new_col='dayofweek')
    
    # group the data by "weather_main"
    by_weather_main = groupings(day_traffic, 
                                new_col="weather_main")\
                                    .sort_values('traffic_volume', ascending = True)
    
    # group the data by "weather_description"
    by_weather_description = groupings(day_traffic,
                                       new_col="weather_description")\
                                           .sort_values('traffic_volume', ascending = True)
    
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
            
    # create a line plot of the monthly grouped data
    create_lineplot(group_by_month, s_1="month", s_2="traffic_volume",
                    chart_title="day_traffic",
                    x="month",
                    y="traffic"
                    )
    
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
    
    create_scatterplot(day_traffic,
                       s_1="temp", 
                       s_2="traffic_volume",
                       xlim_bottom=230)
    
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