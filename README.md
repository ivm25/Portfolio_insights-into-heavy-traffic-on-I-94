# Portfolio: Insights into heavy traffic on I-94

## Aim of the project 

*Identify key indicators of heavy traffic on I-94 highway*

### Business problem: 

1. Identify the key drivers of high traffic volume on I-94

2. Can we take an informed decision about the traffic indicators, communicate to the concerned authorities and come up with away to manage the traffic?

3. Can we convey where to invest/manage infrastructure or money on traffic controls on I-94?

*Assumptions*

- We will not focus on cleaning of data, assuming that it's been fairly cleaned and uploaded on he UCI Machine Learning Repository.

- A station located approximately midway between Minneapolis and Saint Paul recorded the traffic data. 

- Also, the station only records westbound traffic (cars moving from east to west).

- The results therefore will be analysed about the westbound traffic in proximity of the station.


*Source of Data*

https://archive.ics.uci.edu/ml/datasets/Metro+Interstate+Traffic+Volume

*Organisation of Project*

1. *Loading of the data file, absolute source path and loading of the key modules*.

2. *Function definitions and structures*

3. *Data Exploration*

4. *Feature Engineering*

5. *Key Visualisations*

6. *Conclusions*

*Data Dictionary*

- holiday: (Categorical) US National holidays plus regional holiday, Minnesota State Fair
- temp: (Numeric) Average temp in kelvin
- rain_1h: (Numeric) Amount in mm of rain that occurred in the hour
- snow_1h: (Numeric) Amount in mm of snow that occurred in the hour
- clouds_all: (Numeric) Percentage of cloud cover
- weather_main: (Categorical) Short textual description of the current weather
- weather_description: (Categorical) Longer textual description of the current weather
- date_time: (DateTime) Hour of the data collected in local CST time
- traffic_volume: (Numeric) Hourly I-94 ATR 301 reported westbound traffic volume


*Key Insights*

1. Traffic is **higher during the day time** on I-94, especially on the weekdays.

2. Within the business days, there are **specific hours (peaks around 7 and 16)**.

3. On an average, the **month of July shows lower traffic volume**, which is an interesting result and should be investigated further. The **warmer months between (March-October)** show a higher traffic as compared to the colder months.

4. When other numerical factors were taken into account, it appeared that temperature might have some positive correlation with traffic volume, although it doesnt appear to show any significant relation.

5. When the **categorical variables** were analysed, a few intersting insights came out: *Squall* and *Fog* show lower traffic volume, *Shower snow* and *light rain and snow* are outliers, with traffic volume going beyond 5000 on an average.

*Things to do*:

- Analyse the Night time data. ALso create a presentation to explain all the findings.




