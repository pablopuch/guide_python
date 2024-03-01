'''
    13_Ejercicio
    Realizar un algoritmo que lea un número y que muestre su raíz cuadrada y su raíz cúbica
'''

num = int(input('Introduce un numero entero sin decimales: '))

# Para expresar la raiz se utilizan 0.5 para la cuadra y 1/3 para la cubica (convencion)
print(f'La raiz cuadra es {num**0.5} y la raiz cubica es {num**(1/3)}')