import json

info = []

stations = [
    ('Bremerhaven', 'DEHB005', (471474, 5934928)),
    ('Bremen-Nord', 'DEHB004', (474964, 5892465)),
    ('Bremen-Oslebshausen', 'DEHB012', (482270, 5886959)),
    ('Bremen-Hasenburen', 'DEHB013', (479596, 5885403)),
    ('Bremen-Mitte', 'DEHB001', (487658, 5880868)),
    ('Bremen-Ost', 'DEHB002', (494430, 5878954)),
    ('Dobben', 'DEHB006', (488284, 5881036)),
    ('Nordstrase', '-', (485000, 5883368)),
    ('Bremerhaven', 'DEHB011', (473432, 5937454))    
]

for station in stations:
    d = {
        'name': station[0],
        'code': station[1],
        'coords': station[2]
    }
    info.append(d)

res = json.dumps(info)
print(res)