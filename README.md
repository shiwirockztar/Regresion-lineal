# Regresión lineal — Estimación de matrícula

Descripción

Este proyecto implementa una solución básica para estimar la cantidad de estudiantes
matriculados en semestres futuros utilizando regresión lineal simple. Se aprovechan
datos históricos (archivo CSV) con la cantidad de matriculados por año para ajustar
un modelo de la forma:

	y = a x + b

donde `x` es el año, `y` la cantidad de estudiantes matriculados, y `a` y `b` son
los parámetros que se determinan para ajustar la recta a los datos.

Medición de error

Para evaluar la calidad del ajuste se calcula el Mean Absolute Error (MAE), es decir,
la media de los valores absolutos de la diferencia entre los valores reales y los
estimados por la regresión. Un MAE menor indica un mejor ajuste del modelo.

Estructura del repositorio

- `main.py` — Script principal para ejecutar el ajuste y obtener predicciones.
- `test.py` — Pequeños tests o ejemplos de uso.
- `modules/functions.py` — Funciones auxiliares (lectura de CSV, cálculo de parámetros,
  predicción y cálculo de MAE).
- `database/hist_matriculados.csv` — Datos históricos de matrícula usados para el ajuste.

Uso rápido

1. Asegúrese de tener Python 3 instalado.
2. Coloque o verifique los datos en `database/hist_matriculados.csv`.
3. Ejecute:

	python main.py

Los scripts calcularán los parámetros de la regresión, mostrarán las predicciones y
reportarán el MAE sobre los datos provistos.

Contexto educativo

Esta práctica forma parte de la Práctica VII de Informática I — Laboratorio. No se
abordan en profundidad los algoritmos de optimización para encontrar `a` y `b`;
se usa una implementación directa para entender el concepto de regresión lineal y
la evaluación mediante MAE.

Licencia y créditos

Proyecto educativo — adaptar y reutilizar según convenga para prácticas académicas.