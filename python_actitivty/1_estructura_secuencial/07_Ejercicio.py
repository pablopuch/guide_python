'''
    07_Ejercicio
    Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde. 
    Por ejemplo: 1000 minutos son 16 horas y 40 minutos
'''

cont = int(input('Introduce los minutos: '))

h = cont//60

m = cont%60

print(h,'horas', m,'minutos')
