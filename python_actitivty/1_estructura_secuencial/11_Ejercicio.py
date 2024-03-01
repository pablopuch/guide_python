'''
    11_Ejercicio
    Pide al usuario dos números y muestra la "distancia" entre ellos 
    (el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo)
'''

num1 = int(input('Introduce un numero: '))
num2 = int(input('Introduce otro numero: '))

print(f'La distancia desde {num1} hasta {num2} es de {abs(num2-num1)}')