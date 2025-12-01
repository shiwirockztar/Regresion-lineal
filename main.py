import modules.functions as func

import matplotlib.pyplot as plt
import numpy as np

años, estudiantes = func.cargar_datos() # Cargar los datos en dos listas separadas
m, Y = func.calcular_pendiente_interseccion(años, estudiantes) # Calcular pendiente e intersección
print("Pendiente inicial m:", m)
print("Intersección inicial Y:", Y)

predicted = func.linear_regression(años, m, Y) # Obtener los valores predichos usando la regresión lineal
#func.plot_data((años, estudiantes), predicted) # Graficar los datos originales y la regresión lineal

# Realizar una búsqueda de cuadrícula para optimizar m y Y
#min_error = func.funcion_optimizacion(años, estudiantes, m, Y)
min_error = None

if min_error is None:
    min_error = (1.842727272726714, -3637.0, 3.161148325418145)
    
# Encontrar la combinación de m y Y que minimiza el error MAE
print("Mejor pendiente m:", min_error[0])   # Mejor pendiente m: 1.842727272726714
print("Mejor intersección Y:", min_error[1])# Mejor intersección Y: -3637.0
print("Error MAE mínimo:", min_error[2])    # Error MAE mínimo: 3.161148325418145

best_predicted = func.linear_regression(años, min_error[0], min_error[1])
#func.plot_data((años, estudiantes), best_predicted)

best_predicted = func.linear_regression(años, 1.842727272726714, -3637.0)
func.plot_data((años, estudiantes), best_predicted)

#best_predicted = linear_regression(years, 1.8237272727269367, -3599.0)
#plot_data(data, best_predicted, years)