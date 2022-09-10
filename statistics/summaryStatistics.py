import pandas as pd
from LoadData import *

co2_data=loadDataCO2()
GDP_data = loadDataGDP()

print(GDP_data.describe())
print("\n")
print(co2_data.describe())
