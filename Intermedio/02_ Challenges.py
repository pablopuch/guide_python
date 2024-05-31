### CHALLENGES ###

"""
1 EL FAMOSO "FIZZ BUZZ"

Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".

"""

# def fizz_buzz():
    
    
#     # cont = 1
#     # while cont < 101:
#     #     if(cont % 3 == 0 and cont % 5 == 0):
#     #         print("fizzbuzz")
#     #         cont +=1
#     #     elif(cont % 3 == 0):
#     #         print("fizz")
#     #         cont +=1
#     #     elif(cont % 5 == 0):
#     #         print("buzz")
#     #         cont +=1
#     #     else:
#     #         print(cont)
#     #         cont +=1


#     for i in range(1, 101):
#         if(i % 3 == 0 and i % 5 == 0):
#             print("fizzbuzz")
            
#         elif(i % 3 == 0):
#             print("fizz")
            
#         elif(i % 5 == 0):
#             print("buzz")
            
#         else:
#             print(i)
    
    
# fizz_buzz()


"""
2 ¿Es un Anagrama?

 Escribe una función que reciba dos palabras (String) y retorne
 verdadero o falso (Bool) según sean o no anagramas.
 - Un Anagrama consiste en formar una palabra reordenando TODAS
   las letras de otra palabra inicial.
 - NO hace falta comprobar que ambas palabras existan.
 - Dos palabras exactamente iguales no son anagrama.

"""
    

# def anagrama():
#     word_one = input('Introduce una palabra: ')
#     word_two = input('Introduce una palabra: ')

#     if word_one.lower() == word_two.lower(): # si nos dan dos palabras iguales NO son anagrama
#         return False
#     return sorted(word_one.lower()) == sorted(word_two.lower())

# print(anagrama())




"""
3 La sucesión de Fibonacci
 
Escribe un programa que imprima los 50 primeros números de la sucesión
de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de números en 
  la que el siguiente siempre es la suma de los dos anteriores.
  0, 1, 1, 2, 3, 5, 8, 13...

"""

# def fibonacci():
  
#   fibonacci_sequence = [0, 1]
  
#   while (len(fibonacci_sequence) < 50):
    
#     fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    
#   print(fibonacci_sequence)
#   print(len(fibonacci_sequence))
     
     
# fibonacci()


# # Con recursividad


# def fibonacci_recursive(n, sequence=None):
#   if sequence is None:
#     sequence = [0, 1]
    
#   if n <= 2:
#     return sequence[:n]
  
#   if len(sequence) < n:
#     sequence.append(sequence[-1] + sequence[-2])
#     return fibonacci_recursive(n, sequence)
  
#   return sequence

# fibonacci_sequence  = fibonacci_recursive(50)
# print(fibonacci_sequence)
# print(len(fibonacci_sequence))
  
  
  
  
"""
4 ¿Es un número primo?
 
 Escribe un programa que se encargue de comprobar si un número es o no primo.
 Hecho esto, imprime los números primos entre 1 y 100.

"""

# def is_prime(n):

#     if n < 2:
#       return False
    
#     for index in range(2, n):
#       if(n % index == 0):
#         print(f'{n} no es primo')
#         return False
    
#     print(f'{n} es primo')
#     return True
 
  
# list_prime = []
# i = 2

# while i < 101:
#     if is_prime(i) == True:
#       list_prime.append(i)
#       i +=1
#     else:
#       i +=1
    
# print(f'Los numeros primos entre 1 y 100 son {list_prime}') 

# is_prime(7)


"""

7 Invirtiendo cadenas

  Crea un programa que invierta el orden de una cadena de texto
  sin usar funciones propias del lenguaje que lo hagan de forma automática.
  - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"

"""

def inver_text(text):
  
  inver_text = ""

  for i in range(0, len(text)):
    inver_text += text[len(text) - i - 1]
  return inver_text   
    
print(inver_text('Hola mundo'))
