'''
    02_Ejercicio
    Crea un programa que pida dos número enteros al usuario y diga 
    si alguno de ellos es múltiplo del otro. Crea una función EsMultiplo 
    que reciba los dos números, y devuelve si el primero es múltiplo del segundo.
'''


def es_multiplo(a, b):
    if a % b == 0:
        return True
    else:
        return False

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

if es_multiplo(numero1, numero2):
    print(f"{numero1} es múltiplo de {numero2}.")
else:
    print(f"{numero1} no es múltiplo de {numero2}.")
