
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import time
import statistics
from data import independent as x, dependent as y
plt.xlabel("X (input)")
plt.ylabel("Y (output)")
plt.title("MUCKELMETRICS")

class AI:
    #define weights and biases
    def __init__(self, w=4, b=0):
        self.w = w
        self.b = b
        self.hasLearned = False
        self.weight_optimized = False
        self.bias_optimized = False
        self.tolerance = 0.01
    #for checking what y is with personal weights and biases
    def func(self,x) -> int | float:
        return self.w*x+ self.b
            #checking how the squared error changes to determine gradient
   
    def custom_func(self,x:float,w:int,b:int) -> float| int:
        return w*x+b
       
    def train(self, x,y,lr):
            x = np.array(x)
            y = np.array(y)
            epochs = 0
            self.bias_optimized,self.weight_optimized = False,False
            while not self.bias_optimized or not self.weight_optimized:
              epochs += 1
             
              residuals = np.array([self.func(point) - y[int(index)] for index, point in enumerate(x)])
              weight_gradient = np.mean([residuals[i] * x[i] for i in range(len(residuals))])*2
              bias_gradient = np.mean((residuals))*2
              self.weight_optimized = abs(weight_gradient) <= self.tolerance
              self.bias_optimized = abs(bias_gradient) <= self.tolerance
              if not self.weight_optimized:
                self.w -= weight_gradient * lr
              if not self.bias_optimized:
                self.b -= bias_gradient*lr
               
              if self.bias_optimized and self.weight_optimized:
                break
              if epochs == 300000:
                break  
            MSE = np.mean([residual**2 for residual in residuals])
            return f" MSE: {MSE}, epochs: {epochs}, r2: {1 - (MSE / np.mean([(y[i] - np.mean(y))**2 for i in range(len(y))]))}"
#r2 = 1 - MSER/MSEB


 
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

Sutton = AI(2, 50)
while True:
    User=input("Enter action: ").lower().strip()
    if User == "train":
            lr = float(input("enter learning rate: "))
            print(Sutton.train(x,y,lr))
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
        how_long = input(": ")
        Sutton.showFunc(int(how_long))
    if User == "listresiduals":
        Sutton.lr()