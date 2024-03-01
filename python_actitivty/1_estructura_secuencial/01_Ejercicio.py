'''
    01_Ejercicio
    Escribir un programa que pregunte al usuario su nombre, y luego lo salude.
'''

# caso 1 (sin validacíon)

name = str(input('Hola, ¿cúal es tu nombre?: ')) # guardamos lo que usuario nos introduce en una variable de tipo string
input('Encantodo de saludarte ' + name) # imprimimos por pantalla y concatenamos con la variable



'''----------------------------------------------------------------------------------------------------------------------'''



# caso 2 (con validación)

name = str(input('Hola, ¿cúal es tu nombre?: '))# guardamos lo que usuario nos introduce en una variable de tipo string
name.isalpha()# validamos usando el metodo isalpha()

# el metodo isalpha() nos devuelve TRUE he imprime el resultado y si es FALSE imprime un mensaje de error
if name.isalpha():
    print('Encantando de saludarte ' + name)
else:
    print('Nombre incorrecto')