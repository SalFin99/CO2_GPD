import pandas as pd
from LoadData import *

df=pd.read_csv("/Users/salvatorefinizio/github/dataSets/data_portugal.csv", index_col=0, delimiter=";", decimal=",") #load the csv file ("note: remember the limiter next time")

print(df.describe())

