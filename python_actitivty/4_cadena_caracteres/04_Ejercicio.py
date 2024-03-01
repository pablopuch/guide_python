'''
    04_Ejercicio
    Suponiendo que hemos introducido una cadena por teclado 
    que representa una frase (palabras separadas por espacios), 
    realiza un programa que cuente cuantas palabras tiene.
'''
frase = input('Introduce una frase:')
frase = frase.strip()
palabras = frase.split()
num_palabras = len(palabras)

print(num_palabras)