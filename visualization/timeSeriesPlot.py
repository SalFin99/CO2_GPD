import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from LoadData import *

co2_data=loadDataCO2()
GDP_data = loadDataGDP()

sns.set_style("darkgrid")
fig, ax = plt.subplots(2,3, figsize= (20,15))
fig.tight_layout()
#fig.set_size_inches(100, 65)

fig.subplots_adjust(hspace=0.500, wspace=0.2400)

ax[0][0].tick_params(labelrotation = 15)
sns.lineplot(x='Year', y='Annual_CO2_emissions_TperCap', data=co2_data, ax=ax[0][0])

ax[0][1].tick_params(labelrotation = 15)
sns.lineplot(x='Year', y='logAnnual_CO2_emissions_TperCap', data=co2_data, ax=ax[0][1])

ax[0][2].tick_params(labelrotation = 15)
sns.lineplot(x='Year', y='logDiffAnnual_CO2_emissions_TperCap', data=co2_data, ax=ax[0][2])

ax[1][0].tick_params(labelrotation = 15)
sns.lineplot(x='Year', y='GDP_perCap', data=GDP_data, ax=ax[1][0])

ax[1][1].tick_params(labelrotation = 15)
sns.lineplot(x='Year', y='logGDP_perCap', data=GDP_data, ax=ax[1][1])

ax[1][2].tick_params(labelrotation = 15)
sns.lineplot(x='Year', y='logDiffGDP_perCap', data=GDP_data, ax=ax[1][2])

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
fig.tight_layout()  # otherwise the right y-label is slightly clipped

sns.lineplot(x='Year', y='GDP_perCap', data=GDP_data, ax=ax2,color='red')
sns.lineplot(x='Year', y='Annual_CO2_emissions_TperCap', data=co2_data, ax=ax1, color='green')



plt.show()
