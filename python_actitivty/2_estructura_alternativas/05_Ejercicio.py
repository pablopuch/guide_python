'''
    05_Ejercicio
    Escribe un programa que pida un nombre de usuario y una contraseña y 
    si se ha introducido “pepe” y “asdasd” se indica “Has entrado al sistema”, sino se da un error.
'''

name = input('Usuario: ')
password = input('Contraseña: ')


# 1º forma de resolver

if name == 'pepe' and password == 'asdasd':
    print('Has entrado en el sistema')
else:
    print("Error, no tienes acceso")


'''--------------------------------------------------------------------------------------------------'''


# 2º forma de resolver

'''
    La función assert se utiliza para verificar una condición y,
    si es falsa, lanza una excepción AssertionError
'''
assert name == 'pepe' and password == 'asdasd' , 'Error, no tienes acceso'

# Resto del código aquí si la aserción es verdadera
print('Has entrado en el sistema')