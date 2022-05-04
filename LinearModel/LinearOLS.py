from LoadData import *

co2_TperCap = loadDataCO2()
GDP_perCap = loadDataGDP()

reg_ols = sm.OLS(co2_TperCap, GDP_perCap).fit()

print(reg_ols.summary())
