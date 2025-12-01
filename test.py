import matplotlib.pyplot as plt
import modules.functions as func

data = func.cargar_datos()
años = data[0]
Estudiantes = data[1]

m = float((Estudiantes[-1] - Estudiantes[0])/(años[-1] - años[0]))
Y = float(Estudiantes[0] - m*años[0])

predicted = func.linear_regression(años, m, Y)

func.plot_data(data, predicted)