# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 18:00:49 2024

@author: Alexander Ocampo
"""

# Importa las bibliotecas necesarias para el análisis
import pandas as pd
import matplotlib.pyplot as plt
# Cargar la base de datos iris
dataframe = pd.read_csv('iris.data.txt', header=None, names=['longitud_sepalo', 'ancho_sepalo', 'longitud_petalo',
'ancho_petalo', 'especies'])
X = dataframe.drop('especies', axis=1)
y = dataframe['especies'] 

# Crear un gráfico de dispersión para visualizar la relación entre la longitud y el ancho del sépalo para cada clase de flor iris
colors = ['red', 'blue', 'green']
classes = dataframe['especies'].unique()
for i in range(len(classes)):
    plt.scatter(dataframe.loc[dataframe['especies'] == classes[i], 'longitud_sepalo'],
    dataframe.loc[dataframe['especies'] == classes[i], 'ancho_sepalo'],
    color=colors[i], label=classes[i])
    plt.xlabel('longitud del sépalo')
    plt.ylabel('ancho del sépalo')
    plt.legend(loc='best')
    plt.show()
"""Crear un gráfico de dispersión para visualizar la relación entre la longitud y el ancho del pétalo para cada clase de
flor iris"""

colors = ['red', 'blue', 'green']
classes = dataframe['especies'].unique()
for i in range(len(classes)):
     plt.scatter(dataframe.loc[dataframe['especies'] == classes[i], 'longitud_petalo'],
     dataframe.loc[dataframe['especies'] == classes[i], 'ancho_petalo'],
     color=colors[i], label=classes[i])
     plt.xlabel('longitud del pétalo')
     plt.ylabel('ancho del pétalo')
     plt.legend(loc='best')
     plt.show()

# Dividir los datos en conjuntos de entrenamiento y de prueba
train = dataframe.sample(frac=0.8, random_state=0)
test = dataframe.drop(train.index)
# Entrenar el modelo mediante el algoritmo de clasificación KNN
import numpy as np

def knn_classifier(X_train, y_train, X_test, k):
 y_pred = []
 for i in range(X_test.shape[0]):
     distances = np.sqrt(np.sum((X_train - X_test.iloc[i])**2, axis=1))
     nearest = y_train.iloc[np.argsort(distances)[:k]]
     y_pred.append(nearest.value_counts().index[0])
 return y_pred 

# Evaluar el modelo en el conjunto de prueba calculando la precisión
y_test_pred = knn_classifier(train.drop('especies', axis=1), train['especies'], test.drop('especies', axis=1), 5)
accuracy = (test['especies'] == y_test_pred).mean()

print(f'Accuracy: {accuracy:.2f}') 

# Hacer predicciones sobre nuevos datos
new_data = pd.DataFrame({'longitud_sepalo': [5.1, 4.9], 'ancho_sepalo': [3.5, 3.0], 'longitud_petalo': [1.4, 1.4],
'ancho_petalo': [0.2, 0.2]})
y_pred = knn_classifier(X, y, new_data, 5)
print(f'Predictions: {y_pred}') 
# Hacer predicciones sobre nuevos datos
new_data = pd.DataFrame({'longitud_sepalo': [5.1, 4.9], 'ancho_sepalo': [3.5, 3.0], 'longitud_petalo': [1.4, 1.4],
'ancho_petalo': [0.2, 0.2]})
y_pred = knn_classifier(X, y, new_data, 5)
print(f'Predictions: {y_pred}') 
