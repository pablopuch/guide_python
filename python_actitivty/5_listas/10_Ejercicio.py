'''
    10_Ejercicio
    Diseñar el algoritmo correspondiente a un programa, que:

        Crea una tabla (lista con dos dimensiones) de 5x5 enteros.
        Carga la tabla con valores numéricos enteros.
        Suma todos los elementos de cada fila y todos los elementos de cada columna 
        visualizando los resultados en pantalla.
'''
import random

# Crear una tabla de 5x5 enteros con valores iniciales en cero
tabla = [[0 for _ in range(5)]for _ in range(5)]

# Cargar la tabla con valores numéricos enteros
for i in range(5):
    for j in range(5):
        tabla[i][j] = random.randint(0, 10)
        
# Mostrar la tabla
print("Tabla:")
for fila in tabla:
    print(fila)

# Sumar los elementos de cada fila
print("\nSuma de elementos por fila:")
for fila in tabla:
    print(sum(fila))

# Sumar los elementos de cada columna
print("\nSuma de elementos por columna:")
for j in range(5):
    print(sum(tabla[i][j] for i in range(5)))