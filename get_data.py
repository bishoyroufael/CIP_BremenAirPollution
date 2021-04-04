import numpy as np
import pandas as pd
import requests
from io import StringIO
import glob
import os
from halo import Halo

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


@Halo(text='Getting Data From Server ..', spinner='dots')
def get_data_from_stations(stations):
    data_full = pd.DataFrame()
    for station in stations:
        frames = []
        station_code = station[1]
        print("\n [INFO] Getting station: {}".format(station_code))
        for year_increment in range(9):
            payload = {
                'group': 'pollution',
                'period': '1h',
                'timespan': 'custom',
                'start[date]': '01.01.{}'.format(start_year + year_increment),
                'start[hour]': '00',
                'end[date]': '31.12.{}'.format(start_year + year_increment),
                'end[hour]': '24'
            }

            url = 'https://luftmessnetz.bremen.de/station/{}.csv'.format(station_code)
            r = requests.get(url, params=payload)

            cache_res = r.text
            f_l = cache_res.splitlines()[0]
            if f_l.count(';') > 7:#We recieved PM2.5
                df =  pd.read_csv(StringIO(cache_res), sep=';', skiprows=4, header=None, names=["Date","PM10", "PM2.5", "NO2", "NOx", "NO", "O3", "SO2", "CO"], dtype={'Date': str})
            else:
                df =  pd.read_csv(StringIO(cache_res), sep=';', skiprows=4, header=None, names=["Date","PM10", "NO2", "NOx", "NO", "O3", "SO2", "CO"], dtype={'Date': str})
            df['Date'] = pd.to_datetime(df['Date']).apply(lambda x : x.strftime('%s'))
            frames.append(df)
        complete_frame = pd.concat(frames)
        station_code_column = np.full((len(complete_frame)), station_code)
        complete_frame['station_code'] = station_code_column
        data_full = data_full.append(complete_frame)

    if not os.path.exists("data"):
        os.mkdir("data")
    out = './data/full_data.csv'
    print("\n [INFO] Writing the csv to the disk @ {}".format(out))

    print(data_full.shape)
    print(data_full.head())
    data_full.to_csv(out, index=False)



get_data_from_stations(stations)
