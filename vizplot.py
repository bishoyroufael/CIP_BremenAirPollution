import pandas as pd
import glob
import os

data_path="./data"
assert os.path.exists(data_path) == True, "[ Error ] Path Doesn't Exist! please ensure that you saved the data"

paths = glob.glob(data_path + "/*.csv")
for i in paths:
    pdf = pd.read_csv(i, dtype={'Date': str, 'PM10': float})
    pdf.plot(y='PM10', x='Date')
