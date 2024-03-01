'''
    09_Ejercicio
    Una tienda ofrece un descuento del 15% sobre el total de la compra y 
    un cliente desea saber cuánto deberá pagar finalmente por su compra
'''
compra = float(input('Introduce el total de la compra: '))

descuento = 0.15 * compra

print('Descuento del 15% ', descuento)
print('Total de la compra ', compra-descuento)