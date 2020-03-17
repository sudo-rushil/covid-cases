
from collections import namedtuple
import pandas as pd
from coviddata import report, population


Query = namedtuple('Query', ['infected', 'recovered', 'dead', 'population'])

def query_location(report, country, state=None):
    '''
    Search report for infected, recovered, and dead populations for a country (and state).
    '''
    if (country == 'China' or country == 'US') and state:
        sub = report[
            (report['Country/Region'] == country) & (report['Province/State'] == state)
        ]
        return sub['Infected'].iloc[0], sub['Recovered'].iloc[0], sub['Deaths'].iloc[0]

    else:
        sub = report[report['Country/Region'] == country].sum()
        return sub['Infected'], sub['Recovered'], sub['Deaths']


def query_population(population, country):
    '''
    Find population in country.
    '''
    return population.loc[country, '2020']


def query(country):
    '''
    Find all information for input country.
    '''
    infected, recovered, dead = query_location(report, country)
    pop = query_population(population, country)

    return Query(infected, recovered, dead, pop)
