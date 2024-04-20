'''
    02_Ejercicio
    Algoritmo que pida un número y diga si es positivo, negativo o 0.
'''

num = float(input('Introduce un numero:'))

if num == 0:
    print('El numero es 0')
elif num < 0:
    print('El numero es negativo')
else:
    print('El numero es positivo')
