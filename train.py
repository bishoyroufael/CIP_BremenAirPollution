import pandas as pd
import numpy as np
from lib.utils import nan_helper, pad_along_axis
from lib.config import stations
from lib.net import NN 
from sklearn.preprocessing import MinMaxScaler


data = pd.read_csv('./data/full_data.csv')

#Seperate stations
sep_stations = list()
for station in stations:
    df = data [data['station_code'] == str(station[1])].drop(columns='station_code')
    if df['O3'].isnull().all(): #Station should have O3 measurments beside other pollutants measurments!
        continue
    sep_stations.append({
        "station_code": station[1],
        "numpy": df.drop(columns=['O3','Date']).to_numpy().astype(np.float32),
        "o3": df['O3'].to_numpy().astype(np.float32),
        })


#Station measurments are assumed to have the same ending date! i.e arr[-1][0] is same for all arrays
#Padding is done from the beggining of the stations that has fewer values!
max_m = np.max([i['numpy'].shape[0] for i in sep_stations ])

#Interpolate nans and and stations that have fewer dimensions
for dicc in sep_stations:
    nn = dicc['numpy']
    o3 = dicc['o3']
    #=====Interpolate====
    nans, dd = nan_helper(nn)
    nn[nans]= np.interp(dd(nans), dd(~nans), nn[~nans])
    
    nanso, ddo = nan_helper(o3)
    o3[nanso]= np.interp(ddo(nanso), ddo(~nanso), o3[~nanso])
    #====================
    assert np.isnan(np.sum(dicc['numpy'] )) == False or np.isnan(np.sum(dicc['o3'] )) == False , "Nans founds after interpolation!" #should never trigger! 
    if nn.shape[0] < max_m: #pad if less than max measurments
        dicc['numpy'] = pad_along_axis(nn, max_m, 0)
    if o3.shape[0] < max_m:
        dicc['o3'] = pad_along_axis(o3, max_m, 0)
    #dicc['numpy'] = np.delete(dicc['numpy'], 0, axis=1)

x_train, y_train = [],[]
for dicc in sep_stations:
    x_train.append(dicc['numpy'])
    y_train.append(dicc['o3'][...,np.newaxis])

x_train = np.array(x_train, dtype=np.float32)
y_train = np.array(y_train, dtype=np.float32)

x_train = np.reshape(x_train, (x_train.shape[0]*x_train.shape[1], x_train.shape[2]))
y_train = np.reshape(y_train, (y_train.shape[0]*y_train.shape[1], y_train.shape[2]))

# Save npy on disk
np.save('./data/x_train.npy')
np.save('./data/y_train.npy')

s_x = MinMaxScaler()
s_y = MinMaxScaler()
s_y.fit(y_train)
s_x.fit(x_train)
x_train = s_x.transform(x_train)
y_train = s_y.transform(y_train)

x_train = x_train[...,np.newaxis]

print(x_train.shape) #num of stations * num of pollutants, measurments, 1
print(y_train.shape) #num of stations * num of pollutants, measurments 


model = NN()
model.build_network(x_train.shape[1:])
model.compile()
model.summary()
model.train(x_train, y_train, e=1)
model.save()


