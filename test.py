import matplotlib.pyplot as plt
import modules.functions as func
import numpy as np

data = func.cargar_datos()
años = data[0]
Estudiantes = data[1]

m = float((Estudiantes[-1] - Estudiantes[0])/(años[-1] - años[0]))
Y = float(Estudiantes[0] - m*años[0])

print("Pendiente m:", m)
#print("Intersección Y:", Y) 
predicted = func.linear_regression(años, m, Y)

#func.plot_data(data, predicted)

variacion_m = func.crear_vector(m, 6, 6, paso=0.001)
variacion_Y = func.crear_vector(Y, 500, 500)
#variacion_m = func.crear_vector(m, 6, 6, )
#variacion_Y = func.crear_vector(Y, 5, 5)
variacion_MAE = []
for pendiente in variacion_m:
    for interseccion in variacion_Y:
        predicted = func.linear_regression(años, pendiente, interseccion)
        error = func.MAE(np.array(Estudiantes), predicted)
        variacion_MAE.append((pendiente, interseccion, error))

min_error = min(variacion_MAE, key=lambda x: x[2])
print("Mejor pendiente m:", min_error[0])   
print("Mejor intersección Y:", min_error[1])
print("Error MAE mínimo:", min_error[2])