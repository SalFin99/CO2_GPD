from LoadData import *
import statsmodels.api as sm

co2_TperCap = loadDataCO2()
GDP_perCap = loadDataGDP()

GDP_perCap = GDP_perCap['GDP_perCap']

GDP_perCap=sm.add_constant(GDP_perCap)

reg_ols = sm.OLS(co2_TperCap['Annual_CO2_emissions_TperCap'], GDP_perCap).fit()

print(reg_ols.summary())
