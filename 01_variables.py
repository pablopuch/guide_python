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

