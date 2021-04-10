import keras
from keras.models import Sequential
from keras.layers import LSTM, Input, GRU, Dropout
from keras.layers import Dense
from keras.optimizers import Adam

# Demo : https://colab.research.google.com/drive/1FwjQE8I5rODG2UN5h_O8Y_tT-K3MIfzB?usp=sharing

class nn():
    '''
    Reg. NN class for prediction of O3
    '''
    def __init__(self):
        self.model  = Sequential()
    def model_summary(self):
        self.model.summary()
    def optim(self,lr=1e-3):
        return keras.optimizers.Adam(learning_rate=lr)
    def loss(self):
       return keras.losses.MeanSquaredError() 
    def build_network(self, input_shape):
        self.model.add(LSTM(units=128,return_sequences=True,input_shape=(input_shape, 1)))
        self.model.add(Dropout(0.2))
        self.model.add(LSTM(units=64,return_sequences=False))
        self.model.add(Dropout(0.2))
        # self.model.add(LSTM(units=50,return_sequences=True))
        # self.model.add(Dropout(0.2))
        # self.model.add(LSTM(units=50))
        # self.model.add(Dropout(0.2))
        self.model.add(Dense(1))
    def compile(self, lr=1e-3):
        self.model.compile(
            optimizer=self.optim(lr),
            loss=self.loss()
        )
    def train(self,x,y, e = 100, bs = 32):
        self.model.fit(x,y,epochs = e, batch_size = bs)
