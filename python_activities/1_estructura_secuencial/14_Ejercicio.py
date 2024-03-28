'''
    14_Ejercicio
    Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número invertido. 
    Ejemplo, si se introduce 23 que muestre 32
'''

def invertir_numero(numero):
    # Convertir el número a cadena para facilitar la manipulación de los dígitos
    numero_str = str(numero)
    
    # Verificar si el número tiene dos dígitos
    if len(numero_str) != 2:
        return "El número debe tener exactamente dos dígitos."
    
    # Invertir el orden de los dígitos intercambiando el primero con el segundo
    numero_invertido = numero_str[1] + numero_str[0]
    
    return int(numero_invertido)

# Ejemplo de uso

numero = int(input('Introduce un numero de dos cifras: '))
numero_invertido = invertir_numero(numero)
print(f"El número {numero} invertido es: {numero_invertido}")
