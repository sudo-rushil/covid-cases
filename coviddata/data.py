
import os
from datetime import date
import pandas as pd


def get_current_report():
    '''
    Uses today's date to pull the most current JHU situation report
    '''
    today = date.today()

    try:
        endpoint = f'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{today.month:02}-{today.day:02}-{today.year}.csv'
        report = pd.read_csv(endpoint)

    except:
        endpoint = f'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{today.month:02}-{today.day - 1:02}-{today.year}.csv'
        report = pd.read_csv(endpoint)

    report.drop(columns = [
        'Last Update',
        'Latitude',
        'Longitude'
    ], inplace=True)

    report['Infected'] = report['Confirmed'] - report['Deaths'] - report['Recovered']

    return report


def load_population_data():
    '''
    Load population dataframe from world_pop.csv.
    '''
    filepath = os.path.dirname(os.path.abspath(__file__))
    population = pd.read_csv(os.path.join(filepath, 'world_pop.csv'), index_col=0)

    return population


report, population = get_current_report(), load_population_data()
