# Bremen Air Pollution CIP
Creating statistical analysis for better prediction about air pollution in the city of bremen

# Overpass API
**Usage**: Specify the Overpass-QL query and call the query method from the `overpy` library. Please refer to the Overpass language guide in the refrences section on how to formulate the query string


Example:
*i.e Quering power plants inside the city of Bremen*
```
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
```










# Refrences
* [Overpass Language Guide](https://wiki.openstreetmap.org/wiki/Overpass_API/Language_Guide)

