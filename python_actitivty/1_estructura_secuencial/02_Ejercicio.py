'''
    02_Ejercicio
    Calcular el perímetro y área de un rectángulo dada su base y su altura.
'''

base = int(input('Base del rectangulo: '))
altura = int(input('Altura del rectangulo: '))

perimetro = 2*(base + altura)
area = base * altura

print('El perimetro es: ',perimetro,'\nEl area es: ',area)