from iqoptionapi.stable_api import IQ_Option
from sklearn.preprocessing import StandardScaler
from tensorflow import keras
from keras import layers
import tzlocal
import time
import logging
import pandas as pd
import numpy as np
import pandas_ta as ta

from .iq import iqOption

global model
global option
# Create your views here.
def projectOption(request):
    context = {}

    if request.method == "POST":
        email = request.POST["email"]
        passw = request.POST["password"]
        option = iqOption(email,passw)
        model,plt = option.training() 
        if model:
            context = {
                "model":True,
            }
    return render(request,"iq.html",context)

def trade(request):
    while True:
        df = option.get_candles(40)
        df = df.drop(index=df.index[-1])
        df = df.tail(window_size).drop(columns=["Nxt_returns"])
        scaled_data = option.scale_data(df)
        scaled_data = np.array(scaled_data)
        scaled_data = scaled_data.reshape((1,window_size,6))




# 'mugwepeter0@gmail.com','#Mwenyewe12'
class iqOption:
    def __init__(self,email,password):
        self.combined_df = []
        self.money_list = [1,2,5,11,25,56,118,256,512]
        self.cons = 0
        self.email = email
        self.password = password


    def login(self,verbose = False, iq=None, checkConnection = False):
    
        if verbose:
            logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(message)s')

        if iq == None:
            print("Trying to connect to IqOption")
            iq=IQ_Option(self.email,self.password) # YOU HAVE TO ADD YOUR USERNAME AND PASSWORD
            iq.connect()

        if iq != None:
            while True:
                if iq.check_connect() == False:
                    print('Error when trying to connect')
                    print(iq)
                    print("Retrying")
                    iq.connect()
                else:
                    if not checkConnection:
                        print('Successfully Connected!')
                    break
            time.sleep(3)

        iq.change_balance("PRACTICE") #or real
        return iq
    
    def get_candles(self,count):
        self.iq = self.login()
        for goal in ['EURUSD']:
            interval,endtime =120,time.time()
            candles = self.iq.get_candles(goal,interval,count,endtime)
            df = pd.DataFrame(candles,columns=["at","open","min","max","close"])
            # df.at = df['at'].apply(lambda x: date_convert(x))
            df = df.set_index("at")
            df["sma_21"] = df.ta.sma(length=21)
            df["rsi"],df["ema_4"] = df.ta.rsi(),df.ta.ema(length=4)
            df["CandleTravel"] = df["max"] - df["min"]
            df["CandleSize"] = df["close"] - df["open"]

            df["Nxt_close"] = df["close"].shift(-1)
            df["Buy/sell"] = np.where(df.Nxt_close > df.close,1,0)
            df["Returns"] = df["close"].pct_change()
            df["Nxt_returns"] = df["Returns"].shift(-1)

            df_ = df.drop(columns=["min","max","open","close","Nxt_close","Buy/sell"],axis=1)
            df_=df_.dropna()
            self.combined_df.append(df_)
        return pd.concat(self.combined_df)
    
    def scale_data(self):
        scaler = StandardScaler()
        scaled_data = scaler.fit_transform(self.df)
        return scaled_data
    
    def train_sequencing(self):
        self.df = self.get_candles(30000)
        self.scaled_data = self.scale_data()
        self.window_size = 5
        input_sequences = []
        output_labels = []
        for i in range(self.window_size, self.scaled_data.shape[0]):
            input_sequences.append(self.scaled_data[i-self.window_size:i, :6])
            output_labels.append(self.scaled_data[i-1, -1:])

        # Convert input sequences and output labels to Numpy arrays
        input_sequences = np.array(input_sequences)
        print(input_sequences.shape)
        output_labels = np.array(output_labels)

        return input_sequences,output_labels
    
    def predicting(self,y_pred):
    # Convert predictions to buy, sell, or hold recommendations
        recommendations = []
        
        for pred in y_pred:
            if np.argmax(pred) == 0:
                recommendations.append('call')
            elif np.argmax(pred) == 1:
                recommendations.append('put')
            else:
                recommendations.append('hold')
        return recommendations

    def training(self):
        input_sequences,output_labels = self.train_sequencing()
        test_size = 0.2
        split_index = int(len(input_sequences) * (1 - test_size))
        X_train, y_train = input_sequences[:split_index], output_labels[:split_index]
        X_test, y_test = input_sequences[split_index:], output_labels[split_index:]

        # Define the LSTM model architecture
        model = keras.Sequential()
        model.add(layers.LSTM(180, input_shape=(self.window_size, 6)))
        # model.add(layers.Dense(1, activation='linear'))
        model.add(layers.Dense(3, activation='softmax'))

        # Compile and train the model
        model.compile(optimizer='adam', loss='mse')
        # model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
        # model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

        model.fit(X_train, y_train, batch_size=32, epochs=50, validation_split=0.2)
        y_pred = model.predict(X_test)

        # Threshold values for buy and sell recommendations
        buy_threshold = 0.05
        sell_threshold = -0.05

        recommendations = self.predicting(y_pred)
        print()
        buys,sells,loss,lst,cons,c = 0,0,0,[],0,[]
        for i in range(len(y_pred)):
            if recommendations[i] =="sell" and y_test[i] < 0:
                sells +=1
                lst.append("1")
            elif recommendations[i] =="buy" and y_test[i] > 0:
                buys +=1
                lst.append("0")
            elif (recommendations[i]=="sell" and y_test[i] > 0) or (recommendations[i]=="buy" and y_test[i] < 0):
                loss +=1
                lst.append("2")
        for i in range(len(lst)):
            if lst[i] == "2" and lst[i-1] =="2":
                cons +=1
            else:
                c.append(cons)
                cons = 0
        try:
            print(f"ALL>>{len(y_pred)}   loss:{loss} buys:{buys} sells:{sells} loss_percent:{loss/(buys+sells+loss)} consequtive:{max(c)}")
        except ZeroDivisionError:
            pass
        import matplotlib.pyplot as plt

        plt.figure(figsize=(16,8))
        plt.plot(y_test, color = 'black', label = 'Test')
        plt.plot(y_pred, color = 'green', label = 'pred')
        plt.legend()
        return model,plt
    def martingale(self,cons):
        cons+=1
        if cons > len(self.money_list):
            return self.money_list[0]
        money = self.money_list[cons]
        return money,cons


