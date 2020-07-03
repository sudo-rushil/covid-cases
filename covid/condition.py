import numpy as np
import dataclasses
from covid import confirmed, deaths, recovered


@dataclasses.dataclass
class Condition:
    location: str
    date: str
    lat: np.float64
    long: np.float64
    dist: np.float64
    count: np.int64
    recover: np.int64
    deaths: np.int64


def condition(index, distance):
    """
    Constructor function for Condition dataclass that reads
    values from dataset.
    """
    if confirmed["Province/State"][index] is np.nan:
        location = confirmed["Country/Region"][index]
    else:
        location = (
            confirmed["Province/State"][index]
            + ", "
            + confirmed["Country/Region"][index]
        )

    latest = -1

    while np.isnan(confirmed.iloc[index, latest]):
        latest -= 1

    return Condition(
        location,
        confirmed.iloc[index].index[latest],
        confirmed["Lat"][index],
        confirmed["Long"][index],
        distance,
        confirmed.iloc[index, latest],
        0,
        # recovered.iloc[index, latest], # Note: recovered cases aren't working; see changes in results.html
        deaths.iloc[index, latest],
    )
