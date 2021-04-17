'''
Config Constants
'''

CITY = 'Bremen'
BASE_URL = "https://www.umweltbundesamt.de/api/air_data/v2/"
COMPONENTS_URL = "components/json"
NETWORKS_URL = "networks/json"
MEASUREMENT_URL = "measures/json"
SCOPES_URL = "scopes/json"
JSON_OUT_DIR ="./output_json/"
stations = [
    ('Bremerhaven', 'DEHB005', (471474, 5934928)),
    ('Bremen-Nord', 'DEHB004', (474964, 5892465)),
    ('Bremen-Oslebshausen', 'DEHB012', (482270, 5886959)),
    ('Bremen-Hasenburen', 'DEHB013', (479596, 5885403)),
    ('Bremen-Mitte', 'DEHB001', (487658, 5880868)),
    ('Bremen-Ost', 'DEHB002', (494430, 5878954)),
    ('Dobben', 'DEHB006', (488284, 5881036)),
   #('Nordstrase', '-', (485000, 5883368)),
   ('Bremerhaven', 'DEHB011', (473432, 5937454))   # Stations doesn't have o3 measurments 
]
