import os
#os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' 
import tensorflow.keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Input, GRU, Dropout
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from pathlib import Path 
# Demo : https://colab.research.google.com/drive/1FwjQE8I5rODG2UN5h_O8Y_tT-K3MIfzB?usp=sharing

class NN():
    '''
    Reg. NN class for prediction of O3
    '''
    def __init__(self):
        self.model  = Sequential()
        Path.mkdir('./logs', parents=True, exist_ok=True)
        self.tb_callback = tensorflow.keras.callbacks.TensorBoard('./logs', update_freq=1)
    def summary(self):
        self.model.summary()
    def optim(self,lr=1e-3):
        return tensorflow.keras.optimizers.Adam(learning_rate=lr)
    def loss(self):
       return tensorflow.keras.losses.MeanSquaredError() 
    def build_network(self, input_shape, lstm=True):
        self.model.add(Input(shape=input_shape))
        if lstm:
            self.model.add(LSTM(units=128,return_sequences=True, input_shape=input_shape))
            self.model.add(Dropout(0.2))
            self.model.add(LSTM(units=64,return_sequences=True))
            self.model.add(Dropout(0.2))
            #self.model.add(LSTM(units=50,return_sequences=True))
            #self.model.add(Dropout(0.2))
            #self.model.add(LSTM(units=50))
            #self.model.add(Dropout(0.2))
        else:
            self.model.add(Dense(32, kernel_initializer='normal', activation='relu'))
        self.model.add(Dense(1))
    def compile(self, lr=1e-3):
        self.model.compile(
            optimizer=self.optim(lr),
            loss=self.loss()
        )
    def train(self,x,y, e = 50, bs = 32, vs = 0.2):
        self.model.fit(x,y,epochs = e, batch_size = bs, validation_split=vs, callbacks=[self.tb_callback])

    def save(self):
        model_json = self.model.to_json()
        with open("model.json", "w") as json_file:
            json_file.write(model_json)
        # serialize weights to HDF5
        self.model.save_weights("model.h5")
