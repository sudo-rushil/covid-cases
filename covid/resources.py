import pandas as pd
from geopy.geocoders import ArcGIS


def merge_global_us(glob, us):
    us["Province/State"] = us["Admin2"] + ", " + us["Province_State"]
    us["Country/Region"] = us["Country_Region"]
    us["Long"] = us["Long_"]
    new_us = us.drop(columns=us.columns[:8].to_list() + ["Long_", "Combined_Key"])
    return pd.concat([glob, us], join="inner", ignore_index=True)


# Source data
confirmed_global = pd.read_csv(
    "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
)

confirmed_us = pd.read_csv(
    "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv"
)

confirmed = merge_global_us(confirmed_global, confirmed_us)

deaths_global = pd.read_csv(
    "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"
)

deaths_us = pd.read_csv(
    "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv"
)

deaths = merge_global_us(deaths_global, deaths_us)

recovered = pd.read_csv(
    "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv"
)


geolocator = ArcGIS()
