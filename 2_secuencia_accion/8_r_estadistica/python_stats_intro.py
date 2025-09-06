# Cuaderno Jupyter: Introducción a la sintaxis de Python para Estadística Descriptiva

# ================================================================
# 1. Introducción a Python
# ================================================================
# Actividad 1: Crear variables de distintos tipos de datos.

# Ejemplo
entero = 10
flotante = 3.14
cadena = "Hola Python"

print(type(entero))
print(type(flotante))
print(type(cadena))

# ACTIVIDAD ESTUDIANTE:
# 1. Crea una variable entera, una flotante y una de texto con tus propios valores.
# 2. Imprime el tipo de dato de cada variable.

# ================================================================
# 2. Operaciones aritméticas
# ================================================================
# Ejemplo
x = 8
y = 3
print("Suma:", x + y)
print("Resta:", x - y)
print("Multiplicación:", x * y)
print("División:", x / y)
print("Potencia:", x ** y)

# ACTIVIDAD ESTUDIANTE:
# Calcula con tus propias variables: promedio, valor absoluto y residuo (mod).

# ================================================================
# 3. Listas y datos
# ================================================================
# Ejemplo: Lista de calificaciones
calificaciones = [3.5, 4.0, 2.8, 5.0, 3.9]
print("Lista de calificaciones:", calificaciones)
print("Primer elemento:", calificaciones[0])
print("Último elemento:", calificaciones[-1])

# ACTIVIDAD ESTUDIANTE:
# 1. Crea una lista con las edades de 6 compañeros de clase.
# 2. Imprime la edad mayor y menor usando max() y min().

# ================================================================
# 4. Bucles y condicionales
# ================================================================
# Ejemplo: recorrer calificaciones y contar aprobados (>=3.0)
contador = 0
for nota in calificaciones:
    if nota >= 3.0:
        contador += 1
print("Número de aprobados:", contador)

# ACTIVIDAD ESTUDIANTE:
# Escribe un bucle que cuente cuántos de tus compañeros son mayores de edad (>=18).

# ================================================================
# 5. Funciones en Python
# ================================================================
# Ejemplo: función para calcular promedio
def promedio(lista):
    return sum(lista) / len(lista)

print("Promedio calificaciones:", promedio(calificaciones))

# ACTIVIDAD ESTUDIANTE:
# Escribe una función que calcule la varianza de una lista de datos.

# ================================================================
# 6. Estadística descriptiva básica
# ================================================================
import statistics as stats

print("Media:", stats.mean(calificaciones))
print("Mediana:", stats.median(calificaciones))
print("Moda:", stats.mode(calificaciones))
print("Varianza:", stats.variance(calificaciones))
print("Desviación estándar:", stats.stdev(calificaciones))

# ACTIVIDAD ESTUDIANTE:
# Calcula la media, mediana y desviación estándar de la lista de edades de tu grupo.

# ================================================================
# 7. Visualización de datos
# ================================================================
import matplotlib.pyplot as plt

plt.hist(calificaciones, bins=5, edgecolor='black')
plt.title("Histograma de calificaciones")
plt.xlabel("Calificación")
plt.ylabel("Frecuencia")
plt.show()

# ACTIVIDAD ESTUDIANTE:
# Construye un histograma con la lista de edades de tu grupo.
