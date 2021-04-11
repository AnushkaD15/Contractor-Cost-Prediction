import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.linear_model import LinearRegression

df=pd.read_csv("contractor_cost_prediction.csv")

x = dataset.iloc[:, :-1]
y = dataset.iloc[:, 6]
#x=df[['cement','sand','steel','aggregate','mason','skilled_labor']] (dataset in x)
#y=df[['contractor_cost']] (dataset in y)
reg=linear_model.LinearRegression()
reg.fit(x,y)

predictContractorCost= reg.predict([[250,75,55,60,500,562]])
print(predictContractorCost)