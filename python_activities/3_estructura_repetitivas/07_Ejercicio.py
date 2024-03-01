'''
    07_Ejercicio
    Realizar una algoritmo que muestre la tabla de multiplicar de un número introducido por teclado.
'''
num = int(input('Introcuce un nuemero:'))

for i in range(1,11):
    print(num,'X',i,'=',num*i)