'''
    08_Ejercicio
    Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas. 
    El vendedor desea saber cuánto dinero obtendrá por concepto de comisiones por 
    las tres ventas que realiza en el mes y el total que recibirá en el mes tomando 
    en cuenta su sueldo base y comisiones
'''

base = float(input('Introduce el salario base: '))
n = int(input('Numero de ventas: '))

comision = (10*base)/100

print('Comisión por ', n,' ventas es de ', comision*n)
print('El total del sueldo más las comisiones es ', (comision*n)+base)