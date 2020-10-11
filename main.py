'''
IMPORTS
'''
import overpy
import matplotlib.pyplot as plt
import lib.config as cfg

city = cfg.CITY

api = overpy.Overpass()

OVERPASS_QRY = """
area["name"="Bremen"]->.a;
(
  node["power"="plant"](area.a);
  way["power"="plant"](area.a);
  relation["power"="plant"](area.a);
);(._;>;);
out center;  
"""

PWR_PLTS = api.query(OVERPASS_QRY) 


print("Nodes : {}, Ways : {}, Relations : {}".format(
  len(PWR_PLTS.nodes), len(PWR_PLTS.ways), len(PWR_PLTS.relations)))


coords  = []
'''
Append Coordinates (lon, lat) to a list
'''
coords += [(float(node.lon), float(node.lat)) 
           for node in PWR_PLTS.nodes]
coords += [(float(way.center_lon), float(way.center_lat)) 
           for way in PWR_PLTS.ways]
coords += [(float(rel.center_lon), float(rel.center_lat)) 
           for rel in PWR_PLTS.relations]



# coords = []
# for element in data['elements']:
#   if element['type'] == 'node':
#     lon = element['lon']
#     lat = element['lat']
#     coords.append((lon, lat))
#   elif 'center' in element:
#     lon = element['center']['lon']
#     lat = element['center']['lat']
#     coords.append((lon, lat))# Convert coordinates into numpy array
# X = np.array(coords)plt.plot(X[:, 0], X[:, 1], 'o')
# plt.title('Power Plants in Bremen')
# plt.xlabel('Longitude')
# plt.ylabel('Latitude')
# plt.axis('equal')
# plt.show()


# print(PWR_PLTS.nodes)

