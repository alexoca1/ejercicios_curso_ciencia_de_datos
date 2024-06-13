# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
import pandas as pd

data = pd.read_excel("C:\Python spyder\Epidural.xlsx")

import matplotlib.pyplot as plt
import numpy as np

x = data['edad']
y = data['EXPULSIV']

import numpy as np

m, b = np.polyfit(x, y, 1)

plt.scatter(x, y, color='b')
plt.plot(x, m*x + b, color='r', label='linea de Regresion')
plt.xlabel('edad')
plt.ylabel('Expulsividad despues del parto')
plt.title('Diagrama de Dispersion')
plt.legend()
plt.show()