'''
    03_Ejercicio
    Pide una cadena y un carácter por teclado (valida que sea un carácter)
    y muestra cuantas veces aparece el carácter en la cadena.
'''
cadena = input('Intrude una cadena de texto:')
caracter = input('Una letra:')
while len(caracter) != 1:
    print('solo una letra')
    caracter = input('Una letra:')

print(cadena.count(caracter))