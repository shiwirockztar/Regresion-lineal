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

Instalación y entorno virtual (Windows - cmd.exe)

1. Crear un entorno virtual en la carpeta del proyecto:

```cmd
python -m venv .venv
```

2. Activar el entorno virtual (en `cmd.exe`):

```cmd
.\.venv\Scripts\activate
```

3. (Opcional) Actualizar `pip` dentro del venv:

```cmd
python -m pip install --upgrade pip
```

4. Crear un `requirements.txt` mínimo (si no existe):

```cmd
echo numpy > requirements.txt
```

5. Instalar dependencias desde `requirements.txt` (con venv activado):

```cmd
pip install -r requirements.txt
```

6. Verificar que `numpy` está instalado y se puede importar:

```cmd
python -c "import numpy as np; print('numpy OK, versión', np.__version__)"
```

7. Ejecutar el script principal dentro del venv:

```cmd
python main.py
```

8. Salir del venv cuando termines:

```cmd
deactivate
```

Consejos de resolución de problemas
- Si al ejecutar `test.py` sigue apareciendo `ModuleNotFoundError`, añade temporalmente al inicio del script:

```python
import sys
print('Python que ejecuta el script:', sys.executable)
```

- Asegúrate de que el `sys.executable` apunte a `...\.venv\Scripts\python.exe`.
- Si tienes varias versiones de Python instaladas en Windows, usa el launcher `py`:

```cmd
py -3 -m venv .venv
.\.venv\Scripts\activate
py -3 -m pip install -r requirements.txt
```

- Para fijar versiones exactas tras instalar, genera `requirements.txt` con:

```cmd
pip freeze > requirements.txt
```
