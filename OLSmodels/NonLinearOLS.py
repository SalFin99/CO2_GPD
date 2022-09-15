from LoadData import *
import statsmodels.api as sm
import pandas as pd
import numpy as np
from diagnosticTests import *

data = loadAll() #just returns the dataset
data['sqGDP_percap'] = np.square(data['GDP_perCap'])
data['CO2_lag1'] = data['Annual_CO2_emissions_TperCap'].shift(1) #lag column for co2 variable

y=data[['Annual_CO2_emissions_TperCap']] #dependent variable

x=data[['GDP_perCap', 'sqGDP_percap', 'CO2_lag1']] #independent variables
x['dummy1989']=0 #dummy column
x['dummy1999']=0 #dummy columns
x.loc['1989', 'dummy1989']=1 #setting 1 for specific years ...
x.loc['1999', 'dummy1999']=1
x=sm.add_constant(x)



reg_ols = sm.OLS(y, x.astype(float), missing='drop').fit(cov_type='HC3')


print(reg_ols.summary())
