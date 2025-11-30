import modules.functions as func
años, Estudiantes = func.cargar_datos()
#print(len(datos))
#print(años)s
#print(Estudiantes)

m = float((Estudiantes[-1] - Estudiantes[0])/(años[-1] - años[0]))
Y = float(Estudiantes[0] - m*años[0])

predicted = func.linear_regression(años, m, Y)
print(predicted)