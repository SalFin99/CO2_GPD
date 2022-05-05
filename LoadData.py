import pandas as pd
import statsmodels.api as sm

def loadDataGDP():
    df=pd.read_csv("/Users/salvatorefinizio/github/dataSets/data_portugal.csv", index_col=0, delimiter=";", decimal=",") #load the csv file ("note: remember the limiter next time")

    GDP_perCap=df.GDP_perCap #regressor
    GDP_perCap=sm.add_constant(GDP_perCap) #add constant term

    return GDP_perCap

def getGDP():
    df=pd.read_csv("/Users/salvatorefinizio/github/dataSets/data_portugal.csv", index_col=0, delimiter=";", decimal=",") #load the csv file ("note: remember the limiter next time")

    GDP_perCap=df.GDP_perCap #regressor
    return GDP_perCap

def loadDataCO2():
    df=pd.read_csv("/Users/salvatorefinizio/github/dataSets/data_portugal.csv", index_col=0, delimiter=";", decimal=",") #load the csv file ("note: remember the limiter next time")

    co2_TperCap=df.Annual_CO2_emissions_TperCap #response variable

    return co2_TperCap
