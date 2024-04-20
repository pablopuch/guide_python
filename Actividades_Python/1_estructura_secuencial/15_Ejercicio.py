'''
    15_Ejercicio
        Dadas dos variables numéricas A y B, que el usuario debe teclear, 
        se pide realizar un algoritmo que intercambie los valores de 
        ambas variables y muestre cuanto valen al final las dos variables.
'''

A = int(input('Introducir un valor: '))
B = int(input('Introducir un valor: '))


print('A = ' , A)
print('B = ' , B)

# para intercambair valores, necesitamos una variable auxiliar
temp = A
A = B
B = temp

print('Valores intercambiados')
print('A = ' , A)
print('B = ' , B)
