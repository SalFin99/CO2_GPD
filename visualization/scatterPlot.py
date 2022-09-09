import matplotlib.pyplot as plt

from LoadData import *

co2_TperCap = loadDataCO2()
GDP_perCap = getGDP()

plt.plot(GDP_perCap, co2_TperCap, 'o')
plt.show()



