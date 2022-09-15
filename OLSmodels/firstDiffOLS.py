from LoadData import *
import statsmodels.api as sm
import pandas as pd
import numpy as np
from diagnosticTests import *

data = loadAll() #just returns the dataset
data['logDiffGDP_perCap'] = np.log(1+data.GDP_perCap.pct_change())
data['logDiffAnnual_CO2_emissions_TperCap'] = np.log(1+data.Annual_CO2_emissions_TperCap.pct_change())
data['lag1_DiffCO2'] = data['logDiffAnnual_CO2_emissions_TperCap'].shift(1)
data['lag2_DiffCO2'] = data['logDiffAnnual_CO2_emissions_TperCap'].shift(2)

y = data[['logDiffAnnual_CO2_emissions_TperCap']]

x=data[['logDiffGDP_perCap', 'lag1_DiffCO2','lag2_DiffCO2']]
x['dummy1875']=0 #dummy columns
x['dummy1877']=0 #dummy columns
x.loc['1875', 'dummy1875']=1 #setting 1 for specific years....
x.loc['1877', 'dummy1877']=1

x=sm.add_constant(x)

reg_ols = sm.OLS(y, x.astype(float), missing='drop').fit(cov_type='HC3')

print(reg_ols.summary())
