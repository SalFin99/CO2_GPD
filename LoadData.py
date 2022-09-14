import pandas as pd
import numpy as np

def loadAll():
    df=pd.read_csv("/Users/salvatorefinizio/github/dataSets/data_portugal.csv", parse_dates=['Year'], index_col=['Year'] ,delimiter=";", decimal=",") #load the csv file ("note: remember the limiter next time")
    df.index = pd.to_datetime(df.index, format = '%Y/%m/%d').strftime('%Y')
    df.index.name=None

    return df

def loadDataGDP():
    df=pd.read_csv("/Users/salvatorefinizio/github/dataSets/data_portugal.csv", index_col=0, delimiter=";", decimal=",") #load the csv file ("note: remember the limiter next time")
    df=df.drop(['Annual_CO2_emissions_TperCap'], axis=1)  #column dropped because it is useless to load everything, everytime.
    df['logGDP_perCap'] = np.log(df['GDP_perCap'])
    df['logDiffGDP_perCap'] = np.log(1+df.GDP_perCap.pct_change())

    return df

def getGDP():
    df=pd.read_csv("/Users/salvatorefinizio/github/dataSets/data_portugal.csv", index_col=0, delimiter=";", decimal=",") #load the csv file ("note: remember the limiter next time")

    GDP_perCap=df.GDP_perCap #regressor
    return GDP_perCap


def loadDataCO2():
    df=pd.read_csv("/Users/salvatorefinizio/github/dataSets/data_portugal.csv", index_col=0, delimiter=";", decimal=",") #load the csv file ("note: remember the limiter next time")
    df=df.drop(columns=['GDP_perCap']) #column dropped because it is useless to load everything, everytime.
    df['logAnnual_CO2_emissions_TperCap']=np.log(df['Annual_CO2_emissions_TperCap'])
    df['logDiffAnnual_CO2_emissions_TperCap'] = np.log(1+df.Annual_CO2_emissions_TperCap.pct_change())

    return df
