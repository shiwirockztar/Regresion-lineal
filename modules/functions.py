# Módulo que contiene las funciones relacionadas con el procesamiento de datos estadísticos de estudiantes
import csv
import copy

def limpiar_pantalla(espacios = 40):
    # Esta función limpia la pantalla de la consola.
    print("\n"*espacios)
    print("\033[H")   # Secuencia de escape ANSI para mover el cursor a la posición (0,0)
    

def cargar_datos(path = './database/hist_matriculados.csv'):
    # Esta función carga los datos desde un archivo CSV y los devuelve como una lista de diccionarios.
    datos = []
    with open(path,"r") as csvfile:
        cabeceras = csvfile.readline().strip().split(",")
        for linea in csvfile:
            valores = linea.strip().split(",")
            registro = {cabeceras[i]: valores[i] for i in range(len(cabeceras))}
            datos.append(registro)
    return datos