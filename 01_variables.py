# Variables

'''
En python las buenas practicas dictan que hay que seguir unas combenciones
Aquí la estructura a seguir NO ES la de 'camelCase'
En Python es 'snake_case'
'''

# MALA PRACTICA

'''
first-name
first@name
first$name
num-1
1num
'''

myStringVariable = 'Mi variable varia'
print(myStringVariable) # Mi variable varia

# BUENA PRACTICA

'''
firstname
lastname
age
country
city
first_name
last_name
capital_city
_if # queremos utilizar la palabra reservada como variable
year_2021
year2021
current_year_2021
birth_year
num1
num2
'''

my_string_variable = 'Las cosas bien echas, bien salen'
print(my_string_variable) # Las cosas bien echas, bien salen

my_int_variable = 5
print(my_int_variable) # 5

my_bool_variable = True
print(my_bool_variable) # True

# Con print podemos pasarles varía variables y las montará une una cadena

print(my_string_variable, my_int_variable, my_bool_variable) 
# Las cosas bien echas, bien salen 5 True


my_int_to_str_variable = str(my_int_variable) # str() te transforma a string
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))


# Algunas Funciones del sistema

print(len(my_string_variable)) # len() cuenta los caracteres con espacios

print("¿Que tiene esta variable my_string_variable?", my_string_variable)


# Variables en una sola línea. !No te flipes con esto¡

name, surname, alias, age = 'Pablo', 'Puch', 'Poker21', 25
print("Me llamo:", name, surname, ". Mi edad es:", age, ". Y mi alias es:", alias)


first_name = input('What is your name?: ') # input() interactua con la consola 
age = input('How old are you?: ')

print(first_name, age)

# Cambiamos su tipo

name = 22
age = 'Pablo'
print(name, age)

name = 15248
age = 'Manolo'
print(name, age)

address: str = 'Mi dirección' # Forzamos el tipo
address = 55
address = True
print(type(address))