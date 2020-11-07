import numpy as np
import pandas as pd
import requests
from io import StringIO
import os 

start_year = 2010


stations = [
    ('Bremerhaven', 'DEHB005', (471474, 5934928)),
    ('Bremen-Nord', 'DEHB004', (474964, 5892465)),
    ('Bremen-Oslebshausen', 'DEHB012', (482270, 5886959)),
    ('Bremen-Hasenburen', 'DEHB013', (479596, 5885403)),
    ('Bremen-Mitte', 'DEHB001', (487658, 5880868)),
    ('Bremen-Ost', 'DEHB002', (494430, 5878954)),
    ('Dobben', 'DEHB006', (488284, 5881036)),
    ('Bremerhaven', 'DEHB011', (473432, 5937454))
]

for station in stations:
    frames = []
    for year_increment in range(10):
        payload = {
            'group': 'pollution',
            'period': '1h',
            'timespan': 'custom',
            'start[date]': '01.01.{}'.format(start_year + year_increment),
            'start[hour]': '00',
            'end[date]': '31.12.{}'.format(start_year + year_increment),
            'end[hour]': '24'
        }

        station_code = station[1]
        url = 'https://luftmessnetz.bremen.de/station/{}.csv'.format(station_code)
        r = requests.get(url, params=payload)


        df =  pd.read_csv(StringIO(r.text), sep=';', skiprows=4, header=None,names=["Date","PM10", "NO2", "NOx", "NO", "O3", "SO2", "CO"])
        print(df.head())
        frames.append(df)

    complete_frame = pd.concat(frames)

    if not os.path.exists("data"):
        os.mkdir("data")
    out = './data/{}.csv'.format(station_code)
    complete_frame.to_csv(out)
