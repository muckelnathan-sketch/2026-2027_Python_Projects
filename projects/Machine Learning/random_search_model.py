import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import time
from data import independent as x, dependent as y
plt.xlabel("X (input)")
plt.ylabel("Y (output)")
plt.title("MUCKELMETRICS")

class AI:
    def __init__(self, w=50, b=100,):
        self.w = w
        self.b = b
        self.hasLearned = False
    def func(self,x):
        return self.w*x+ self.b
   
    def train(self, x,y,epochs):
        BMSE = {
            'SE':1000000,
            'W': 1000000000,
            'B': 1000000000000
        }
        for i in range(epochs):
            
            residuals = []
            for index, point in enumerate(x):
                residual = self.func(point) - y[index]
                residuals.append(residual)
   
            MSE = (sum(r*r for r in residuals)/len(residuals))

            if MSE <= BMSE['SE']:
                print("new best score found!")
                BMSE['SE'] = MSE
                BMSE['W'] = self.w
                BMSE['B'] = self.b
               
            self.w = random.uniform(-max(y),max(y)/2)
            self.b = random.uniform(min(y),max(y))
        print("done training!")
        self.w = BMSE['W']
        self.b = BMSE['B']
        print(BMSE)
        self.hasLearned = True
    def predict(self,X):
        if self.hasLearned:
            print("predicting...")
            time.sleep(2)
            print(f"I predict that at point {X} the dependent variable will be {round(self.func(float(X)),2)}")
        else:print("AI has not learned yet")
    def showFunc(self,duration):
        print(self.w, self.b)
        plt.scatter(x,y)
        x_start = min(x)
        x_end = max(x)
        y_start = self.func(x_start)
        y_end = self.func(x_end)
        plt.plot([x_start, x_end], [y_start, y_end], color='red')
        plt.draw()
        plt.pause(duration)  
        plt.close()
    def lr(self):
        df = pd.DataFrame({
            'Predicted': [self.func(point) for point in x],
            'Actual': y,
            'Residual': [self.func(point) - y[i] for i, point in enumerate(x)]
        })
   
        print(df)    

Sutton = AI()
while True:
    User=input("Enter action: ").lower().strip()
    if User == "train":
        epochs = input("How many epochs: ")
        try:
            int(epochs)
        except ValueError:
            print("thats not a number!")
        else:
            epochs = int(epochs)
            Sutton.train(x,y,epochs)
    if User == "predict":
        prediction = input("enter input: ")
        try:
            int(prediction)
        except ValueError:
            print("thats not a valid input")
        else:
            prediction = int(prediction)
            Sutton.predict(prediction)
    if User == "graph":
        duration = int(input(": "))
        Sutton.showFunc(duration)
    if User == "listresiduals":
        Sutton.lr()