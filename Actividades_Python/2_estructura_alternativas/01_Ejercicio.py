'''
    01_Ejercicio
    Algoritmo que pida dos números e indique si el primero es mayor que el segundo o no.
'''
first_num = int(input('Introduce un numero: '))
secon_num = int(input('Introduce otro numero: '))

def calular_num_mayor(first_num, secon_num):
    if(first_num > secon_num):
        return print(f'El primer numero {first_num} es mayor que el segundo numero que es {secon_num}')
    else:
        return print(f'El segundo numero {secon_num} es mayor que el primero {first_num}')


calular_num_mayor(first_num, secon_num)