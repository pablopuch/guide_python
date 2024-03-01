'''
    01_Ejercicio
    Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10) y 
    posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado y su cubo.
'''
import random

list_valores = []
list_cuadrada = []    
list_cubo = []   

for _ in range(10):
    list_valores.append(random.randint(1, 10))
    
print(list_valores)
   
   
for num in list_valores:
    cuadrado = num ** 2
    list_cuadrada.append(cuadrado)
    cuadrado = num ** 3
    list_cubo.append(cuadrado)
    
print(list_cuadrada)
print(list_cubo)