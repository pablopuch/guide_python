'''
    02_Ejercicio
    Realizar un programa que comprueba si una cadena leída por teclado 
    comienza por una subcadena introducida por teclado.
'''

cadena = input('Intrude una cadena de texto:')
subcadena = input('Introduce una subcadena de texto:')


if cadena.startswith(subcadena):
    print('La cadena empiza por la subcadena')
else:
    print("No se encuentra")