from LoadData import *
import statsmodels.api as sm
import pandas as pd
import numpy as np

data = loadAll() #just returns the database

data['GDP_lag1'] = data['GDP_perCap'].shift() #lag column for GDP variable
data['CO2_lag1'] = data['Annual_CO2_emissions_TperCap'].shift() #lag column for co2 variable

y=data[['Annual_CO2_emissions_TperCap']] #independet variable

x=data[['GDP_perCap', 'GDP_lag1', 'CO2_lag1']] #regressors

x['dummy']=0 #dummy columns
x.loc['1989', 'dummy']=1 #setting 1 for specific years....
x.loc['2003', 'dummy']=1

x['GDP_lag1']=x['GDP_lag1'].fillna(0) #fixing na values
x['CO2_lag1']=x['CO2_lag1'].fillna(0)

x=sm.add_constant(x)

reg_ols = sm.OLS(y, x).fit()
reg_ols.get_robustcov_results(cov_type='HC3')

print(reg_ols.summary())
