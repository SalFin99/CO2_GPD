from LoadData import *
import statsmodels.api as sm
import pandas as pd

data = loadAll()

data['GDP_lag1'] = data['GDP_perCap'].shift()

y=data[['Year','Annual_CO2_emissions_TperCap']]
print(y)

x=data[['Year','GDP_perCap', 'GDP_lag1']]
x['GDP_lag1']=x['GDP_lag1'].fillna(0)
sm.add_constant(x)


reg_ols = sm.OLS(y, x).fit()

print(reg_ols.summary())
