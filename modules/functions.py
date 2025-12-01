# Módulo que contiene las funciones relacionadas con el procesamiento de datos estadísticos de estudiantes
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

import csv
import copy

def limpiar_pantalla(espacios = 40):
    # Esta función limpia la pantalla de la consola.
    print("\n"*espacios)
    print("\033[H")   # Secuencia de escape ANSI para mover el cursor a la posición (0,0)
    

def cargar_datos_dic(path = './database/hist_matriculados.csv'):
    # Esta función carga los datos desde un archivo CSV y los devuelve como una lista de diccionarios.
    datos = []
    with open(path,"r") as csvfile:
        cabeceras = csvfile.readline().strip().split(",")
        for linea in csvfile:
            valores = linea.strip().split(",")
            registro = {cabeceras[i]: valores[i] for i in range(len(cabeceras))}
            datos.append(registro)
    return datos

def cargar_datos(path = './database/hist_matriculados.csv'):
    # Esta función carga los datos desde un archivo CSV y los devuelve como una lista.
    años = []
    Estudiantes = []
    with open(path,"r") as csvfile:
        cabeceras = csvfile.readline().strip().split(",")
        for linea in csvfile:
            valores = linea.strip().split(",")
            años.append(int(valores[0]))
            Estudiantes.append(int(valores[1]))
    return años, Estudiantes

def calcular_pendiente_interseccion(años, Estudiantes):
    # Esta función calcula la pendiente (m) y la intersección (Y) de la línea de regresión lineal.
    m = float((Estudiantes[-1] - Estudiantes[0])/(años[-1] - años[0]))
    Y = float(Estudiantes[0] - m*años[0])
    return m, Y 

def linear_regression(años, m, Y):
    x = np.array(años)  # Asegurarse de que x sea un arreglo de NumPy
    return x * m + Y

def MAE(y, y_pred):
    return np.mean(np.abs(y - y_pred))

def crear_vector(numero, rebaja, sube, paso=1):
    '''
    Crea un vector con un número repetido desde un límite inferior hasta un límite superior

    numero (int/float): número a repetir
    rebaja (int): cantidad a restar al número para el límite inferior
    sube (int): cantidad a sumar al número para el límite superior

    return (list): vector con el número repetido
    '''
    vector = np.arange(numero - rebaja, numero + sube + 1, paso)
    return vector

def funcion_optimizacion(años, Estudiantes, m, Y):
    '''
    Realiza una búsqueda de cuadrícula para optimizar m y Y

    años (list): lista de años
    Estudiantes (list): lista de estudiantes
    m (float): pendiente inicial
    Y (float): intersección inicial

    return (tuple): mejor pendiente, mejor intersección, error MAE mínimo
    '''
    variacion_m = crear_vector(m, 5, 5, paso=0.001)
    variacion_Y = crear_vector(Y, 300, 300)
    variacion_MAE = []
    for pendiente in variacion_m:   
        for interseccion in variacion_Y:
            predicted = linear_regression(años, pendiente, interseccion)
            error = MAE(np.array(Estudiantes), predicted)
            variacion_MAE.append((pendiente, interseccion, error))  

    # Encontrar la combinación de m y Y que minimiza el error MAE
    min_error = min(variacion_MAE, key=lambda x: x[2])
    return min_error


def plot_data(data, regression_line):
    '''
    Grafica los datos y la Regresión Lineal

    data (tuple of lists): ([años], [estudiantes])
    regression_line (list): valores predichos
    years (list): lista de años correspondiente a regression_line
    '''

    # Separar los datos
    años = np.array(data[0])
    Estudiantes = np.array(data[1])

    # Calcular error MAE
    error = MAE(Estudiantes, regression_line)
    print(error)

    # Graficar
    plt.figure(figsize=(10, 6))
    plt.plot(años, Estudiantes, 'o', label='Data Points')
    plt.plot(años, regression_line, 'r', label='Linear Regression')
    plt.grid(True)
    plt.legend()
    plt.title(f'Historical Data and Linear Regression MAE = {error:.2f}')
    plt.xlabel('Year')
    plt.ylabel('Students Enrolled')
    plt.show()
