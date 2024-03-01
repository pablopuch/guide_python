'''
    18_Ejercicio
    Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.
'''

name = str(input('Escribe tu nombre: '))
surname_first = str(input('Escribe tu primer apellido: '))
surname_second = str(input('Escribe tu segundo apellido: '))

# guardamos en una misma variable y la concatenamos con nombre_variable +
letter = name[0].upper()
letter = letter + surname_first[0].upper()
letter = letter + surname_second[0].upper()

print(letter)