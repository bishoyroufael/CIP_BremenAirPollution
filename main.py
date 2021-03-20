import requests
from lib import config
import json
import time
import os
def request_and_write_to_json(url, strr, param=None):
  r = requests.get(url, param)
  if r.status_code == 200:
    res_json = r.json()
    print("[ INFO ] Exporting {} to json ..".format(strr))
    json_object = json.dumps(res_json, indent = 4) 
    
    try:
      os.mkdir(config.JSON_OUT_DIR)
    except:
      pass

    with open("{}{}.json".format(config.JSON_OUT_DIR,strr), "w") as outfile: 
      outfile.write(json_object) 
  else:
    print("[ ERROR ] GET request failed with status code {}".format(r.status_code))


def get_components():
  request_and_write_to_json(config.BASE_URL+config.COMPONENTS_URL, "components")


def get_networks():
  request_and_write_to_json(config.BASE_URL+config.NETWORKS_URL, "networks")


def get_scopes():
  request_and_write_to_json(config.BASE_URL+config.SCOPES_URL, "scopes")


def get_all_measurements(si, df, dt, tf, tt, ci, sc):
  '''
  Function that outputs the measurments of a specified component id within a specific date range
  as a json on disk

  Args:
  si : station id -> integer
  df : data from -> string <YYYY-MM-DD> 
  dt : data to -> string <YYYY-MM-DD> 
  tf: time from -> integer [ 1 .. 24 ] 
  tt: time to -> integer [ 1 .. 24 ] 
  ci: component id -> integer
  sc: scope -> integer
  '''

  params = {
    "date_from":df,
    "date_to":dt,
    "time_from":tf,
    "time_to":tt,
    "station":si,
    "component":ci,
    # "scope":sc
  }

  request_and_write_to_json(config.BASE_URL+config.MEASUREMENT_URL, "measurements_station_{}_cmp_id_{}".format(si, ci), params)



get_components()
get_scopes()

Bremen_Station_IDs=["DEHB005","DEHB004","DEHB012",13, 6, 11,"012","013"]

for i in Bremen_Station_IDs:
  get_all_measurements(i,"2015-01-01","2016-12-30",1,5,1,2)
  time.sleep(0.5)