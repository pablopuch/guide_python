'''
    11_Ejercicio
    Escribe un programa que diga si un número introducido por teclado es o no primo. 
    Un número primo es aquel que sólo es divisible entre él mismo y la unidad. Nota: 
    Es suficiente probar hasta la raíz cuadrada del número para ver si es divisible 
    por algún otro número.
'''
num = int(input('Introcuce un nuemero:'))

# def primo(num):
#     if num < 2:
#         return 'No es primo'
#     for i in range(2,num):
#         if num % i == 0:
#             return 'No es primo'
#     return 'Es primo'

# print(primo(num))

'''-------------------------------------------------------------------------------------'''

import sympy

def primo(num):
    return sympy.isprime(num)

print(primo(num))