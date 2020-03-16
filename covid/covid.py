
import numpy as np
import pandas as pd
from geopy import distance
from covid import confirmed, condition, geolocator


def search_cases(lat, long, area = 40):
    '''
    Search dataframe for indexes of all cases and their distance to the query (lat, long).
    Within zone defined by area.
    Returns deque() containing indexes and their distance from the query, sorted by distance.
    '''
    subspace = confirmed[((confirmed['Lat'] < lat + area) & (confirmed['Lat'] > lat - area)) \
                        & ((confirmed['Long'] < long + area) & (confirmed['Long'] > long - area))]

    results = []

    for index, data in subspace.iterrows():
        results.append((index, distance.distance((lat, long), (data['Lat'], data['Long'])).miles))

    return sorted(results, key = lambda x: x[-1])


def condition_in_radius(case_indexes, radius = 100):
    '''
    Finds the conditions in all reported areas inside the radius.
    Takes input of list with tuples of (index, distance).
    Returns a list of conditions by distance that can be rendered.
    '''
    search_indexes = ((c, d) for (c, d) in case_indexes if d <= radius)

    return list(filter(lambda cond: cond.count != 0, map(lambda elem: condition(elem[0], elem[1]), search_indexes)))
    # return list(map(lambda elem: condition(elem[0], elem[1]), search_indexes))


def query(query):
    '''
    Runs a full query from the input location string.
    Returns the top 100 places, top 1000 places, and the closest place.
    '''
    location = geolocator.geocode(query)
    cases = search_cases(location.latitude, location.longitude)
    conditions = condition_in_radius(cases, 1000)

    return condition_in_radius(cases), list(filter(lambda cond: cond.dist >= 100, conditions)), conditions[0]
