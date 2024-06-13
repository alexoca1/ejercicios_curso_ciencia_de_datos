# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 23:48:28 2024

@author: casa
"""

import pandas as pd

data = pd.read_excel("Epidural.xlsx")

print(data.columns)

print(data[["edad"]].describe())

epidural_si = data.loc[data["EPIDURAL"] == 1]

data["edad_recodificada"] = pd.cut(data['edad'], bins=[-float('inf'), 24, 25, float('inf')], 
labels=['por debajo', 'por igual', 'por encima']) 

frecuency_table = data['edad_recodificada'].value_counts()

mean =data[['TEMP1', 'TEMP2']].mean(axis=1)
data['TEMP_MEDIA'] = mean
