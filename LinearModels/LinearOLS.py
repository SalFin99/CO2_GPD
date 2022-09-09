from LoadData import *

co2_TperCap = loadDataCO2()
GDP_perCap = loadDataGDP()
sm.add_constant(GDP_perCap)

reg_ols = sm.OLS(co2_TperCap['Annual_CO2_emissions_TperCap'], GDP_perCap['GDP_perCap']).fit()

print(reg_ols.summary())
