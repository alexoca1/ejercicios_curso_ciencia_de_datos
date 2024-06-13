# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 21:56:54 2024

@author: casa
"""


import pandas as pd
import numpy as np
import scipy
import matplotlib as mpl
import matplotlib.pyplot as plt


# importar la base de datos iris

dataframe = pd.read_csv('iris.data.txt', header=None, names=['longitud_sepalo', 'ancho_sepalo', 'longitud_petalo', 'ancho_petalo', 'especies'])

# Explorar los datos mediante tablas de frecuencias y de contingencia 
# tabla de frecuencias de la variable 'especies' 
print(dataframe.groupby('especies').size()) 
# tabla cruzada 
cols = ['longitud_sepalo', 'ancho_sepalo', 'longitud_petalo', 'ancho_petalo', 'especies'] 
dataframe = dataframe[cols] 
cross_tab = pd.pivot_table(dataframe, index='especies', aggfunc='mean') 
print(cross_tab) 

# Calcular el K-Means 
from scipy import stats 
from scipy.stats import mode 
from scipy.cluster.vq import kmeans, vq 
x = dataframe.iloc[:, :-1].values 
centroids, labels = kmeans(x, 3) 
centers = centroids 
labels, _ = vq(x, centroids) 


# Graficamos los puntos y los clusters 
plt.scatter(x[:,0], x[:,1], c=labels) 
plt.scatter(centers[:,0], centers[:,1], marker='*', s=200, c='#050505') 
plt.show() 


# Evaluar el modelo 
# Suma de cuadrados intra-cluster (SSW) 
def ssw(x, labels, centroids): 
 ssw = 0 
 for i in range(len(centroids)): 
     cluster = x[labels == i] 
     ssw += np.sum((cluster - centroids[i])**2) 
 return ssw 
print('SSW:', ssw(x, labels, centroids)) 
# Suma de cuadrados inter-cluster (SSB) 
def ssb(x, labels, centroids): 
 ssb = 0 
 mean = np.mean(x, axis=0) 
 for i in range(len(centroids)): 
     cluster = x[labels == i] 
     ssb += len(cluster) * np.sum((centroids[i] - mean)**2) 
 return ssb 
print('SSB',ssb(x, labels, centroids))
