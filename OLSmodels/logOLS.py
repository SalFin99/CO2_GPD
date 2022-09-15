from LoadData import *
import statsmodels.api as sm
import pandas as pd
import numpy as np
from diagnosticTests import *

data = loadAll() #just returns the dataset
data['logGDP_perCap'] = np.log(data['GDP_perCap'])
data['logCO2']=np.log(data['Annual_CO2_emissions_TperCap'])
data['lag_logCO2'] = data['logCO2'].shift(1)

y=data[['logCO2']] #dependent variable



x=data[['logGDP_perCap', 'lag_logCO2']]
x['dummy1872']=0 #dummy column
x['dummy1874']=0 #dummy columns
x['dummy1877']=0 #dummy columns
x.loc['1872', 'dummy1872']=1 #setting 1 for specific years....
x.loc['1874', 'dummy1874']=1
x.loc['1877', 'dummy1877']=1

x=sm.add_constant(x)

reg_ols = sm.OLS(y, x.astype(float), missing='drop').fit(cov_type='HC3')

print(reg_ols.summary())
