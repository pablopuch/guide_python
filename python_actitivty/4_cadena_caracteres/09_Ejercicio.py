'''
    09_Ejercicio
    Realizar un programa que compruebe si una cadena contiene una subcadena. 
    Las dos cadenas se introducen por teclado.
'''
cadena = input('Intrude una cadena de texto:')
subcadena = input('Introduce una subcadena de texto:')


if cadena.startswith(subcadena):
    print('La cadena empiza por la subcadena')
else:
    print("No se encuentra")
    

'''-------------------------------------------------------------------------'''


if subcadena in cadena:
    print ('Se encontro el substring dentro del string.')
else:
    print ("Substring no encontrado.")